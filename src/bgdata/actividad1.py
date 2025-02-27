import sqlite3
import requests
import json
import pandas as pd

# -------- 1. Obtener datos desde el API --------
def get_data_api(url="", params={}):
    url = "{}/{}/{}/".format(url, params["coin"], params["method"])
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as error:
        print(error)
        return {}

    # Configuración del API
parameters = {"coin": "BTC", "method": "ticker"}
url = "https://www.mercadobitcoin.net/api"
datos = get_data_api(url=url, params=parameters)

# -------- 2. Conectar a SQLite y crear la base de datos --------
conn = sqlite3.connect("big_data.db")
cursor = conn.cursor()

# Crear la tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS crypto_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    high REAL,
    low REAL,
    vol REAL,
    last REAL,
    buy REAL,
    sell REAL,
    date INTEGER
)
""")

# -------- 3. Insertar datos en la base de datos --------
if "ticker" in datos:
    ticker = datos["ticker"]
    cursor.execute("""
    INSERT INTO crypto_data (high, low, vol, last, buy, sell, date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (ticker["high"], ticker["low"], ticker["vol"], ticker["last"], ticker["buy"], ticker["sell"], ticker["date"]))

    conn.commit()
    print("Datos insertados en la base de datos.")
else:
    print("No se encontraron datos para insertar.")

# -------- 4. Generar archivo de muestra (CSV y Excel) --------
df = pd.read_sql_query("SELECT * FROM crypto_data", conn)
df.to_csv("muestra_datos.csv", index=False)
df.to_excel("muestra_datos.xlsx", index=False)
print("Archivo de muestra generado: muestra_datos.csv y muestra_datos.xlsx")

# -------- 5. Generar archivo de auditoría --------
cursor.execute("SELECT high, low, vol, last, buy, sell, date FROM crypto_data ORDER BY id DESC LIMIT 1")
db_data = cursor.fetchone()

conn.close()

with open("auditoria.txt", "w", encoding="utf-8") as audit_file:
    audit_file.write("Comparación de datos entre API y Base de Datos\n")
    audit_file.write("="*50 + "\n")

    if "ticker" in datos and db_data:
        api_ticker = datos["ticker"]
        db_values = list(db_data)
        api_values = [api_ticker["high"], api_ticker["low"], api_ticker["vol"], api_ticker["last"], api_ticker["buy"], api_ticker["sell"], api_ticker["date"]]

        differences = []
        for i, field in enumerate(["high", "low", "vol", "last", "buy", "sell", "date"]):
            if db_values[i] != api_values[i]:
                differences.append(f"{field}: API={api_values[i]}, DB={db_values[i]}")

        if differences:
            audit_file.write("Diferencias encontradas:\n")
            audit_file.writelines("\n".join(differences))
        else:
            audit_file.write("No se encontraron diferencias entre los datos del API y la base de datos.")
    else:
        audit_file.write("No se encontraron datos para comparar.")

print("Archivo de auditoría generado: auditoria.txt")

