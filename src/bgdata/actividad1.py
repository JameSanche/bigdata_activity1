import sqlite3
import requests
import json
import pandas as pd

# -------- 1. Obtener datos desde el API --------
def get_data_api(url, params=None):
    """
    - url: URL base de la API.
    - params: Diccionario con parámetros GET (?name=mario).
    """
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(f"Error al obtener datos: {error}")
        return {}

# -------- 2. Configuración de API y Base de Datos --------
url_amiibo = "https://www.amiiboapi.com/api/amiibo/"
params_amiibo = {"name": "mario"}  # Cambia el nombre según el personaje que quieras buscar

datos = get_data_api(url_amiibo, params_amiibo)

# -------- 3. Mostrar datos en consola --------
if "amiibo" in datos:
    print("\nDatos obtenidos de la API de Amiibo:")
    for amiibo in datos["amiibo"]:
        print(f"Nombre: {amiibo['name']}, Personaje: {amiibo['character']}, "
              f"Serie: {amiibo['amiiboSeries']}, Juego: {amiibo['gameSeries']}, Tipo: {amiibo['type']}")
else:
    print("No se encontraron datos en la API.")

# -------- 4. Conectar a SQLite y crear la base de datos --------
conn = sqlite3.connect("big_data.db")
cursor = conn.cursor()

# Crear tabla para almacenar Amiibos si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS amiibo_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    character TEXT,
    amiiboSeries TEXT,
    gameSeries TEXT,
    type TEXT
)
""")

# -------- 5. Insertar datos en la base de datos --------
if "amiibo" in datos:
    for amiibo in datos["amiibo"]:
        cursor.execute("""
        INSERT INTO amiibo_data (name, character, amiiboSeries, gameSeries, type)
        VALUES (?, ?, ?, ?, ?)
        """, (amiibo["name"], amiibo["character"], amiibo["amiiboSeries"], amiibo["gameSeries"], amiibo["type"]))

    conn.commit()
    print("\nDatos insertados en la base de datos.")
else:
    print("No se encontraron datos para insertar.")

# -------- 6. Generar archivo de muestra (CSV y Excel) --------
df = pd.read_sql_query("SELECT * FROM amiibo_data", conn)
df.to_csv("muestra_datos.csv", index=False)
df.to_excel("muestra_datos.xlsx", index=False)
print("\nArchivo de muestra generado: muestra_datos.csv y muestra_datos.xlsx")

# -------- 7. Generar archivo de auditoría --------
cursor.execute("SELECT name, character, amiiboSeries, gameSeries, type FROM amiibo_data ORDER BY id DESC LIMIT 1")
db_data = cursor.fetchone()

conn.close()

with open("auditoria.txt", "w", encoding="utf-8") as audit_file:
    audit_file.write("Comparación de datos entre API y Base de Datos\n")
    audit_file.write("=" * 50 + "\n")

    if "amiibo" in datos and db_data:
        api_amiibo = datos["amiibo"][0]  # Tomamos el primer resultado
        db_values = list(db_data)
        api_values = [api_amiibo["name"], api_amiibo["character"], api_amiibo["amiiboSeries"], api_amiibo["gameSeries"], api_amiibo["type"]]

        differences = []
        for i, field in enumerate(["name", "character", "amiiboSeries", "gameSeries", "type"]):
            if db_values[i] != api_values[i]:
                differences.append(f"{field}: API={api_values[i]}, DB={db_values[i]}")

        if differences:
            audit_file.write("Diferencias encontradas:\n")
            audit_file.writelines("\n".join(differences))
        else:
            audit_file.write("No se encontraron diferencias entre los datos del API y la base de datos.")
    else:
        audit_file.write("No se encontraron datos para comparar.")

print("\nArchivo de auditoría generado: auditoria.txt")
