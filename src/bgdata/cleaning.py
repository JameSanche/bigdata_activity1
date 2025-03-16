import sqlite3
import pandas as pd
import random

print("Cargando datos desde la base de datos original...")
conn_original = sqlite3.connect("big_data.db")
df = pd.read_sql_query("SELECT * FROM amiibo_data", conn_original)
conn_original.close()

print(f"Registros cargados: {df.shape[0]}")

# Ensuciar datos con valores nulos
def ensuciar_datos(df, porcentaje=0.1):
    df_dirty = df.copy()
    num_filas = df_dirty.shape[0]
    num_filas_afectadas = int(num_filas * porcentaje)

    for col in df_dirty.columns:
        filas_a_modificar = random.sample(range(num_filas), num_filas_afectadas)
        df_dirty.loc[filas_a_modificar, col] = None  

    return df_dirty

df = ensuciar_datos(df, porcentaje=0.1)

# Análisis inicial
num_registros_inicial = df.shape[0]
duplicados = df.duplicated().sum()
valores_nulos = df.isnull().sum().sum()

print(f"Duplicados detectados: {duplicados}, Valores nulos detectados: {valores_nulos}")

# Limpieza de datos
df_cleaned = df.drop_duplicates().dropna()
num_registros_final = df_cleaned.shape[0]

print(f"Limpieza completada. Registros finales: {num_registros_final}")

# Guardar datos limpios en nueva base de datos
conn_cleaned = sqlite3.connect("cleaned_data.db")
df_cleaned.to_sql("amiibo_data_cleaned", conn_cleaned, if_exists="replace", index=False)
conn_cleaned.close()

# Exportar datos limpios
df_cleaned.to_csv("cleaned_data.csv", index=False)

# Generar reporte de auditoría
with open("cleaning_report.txt", "w", encoding="utf-8") as report:
    report.write(f"Registros iniciales: {num_registros_inicial}\n")
    report.write(f"Duplicados eliminados: {duplicados}\n")
    report.write(f"Valores nulos eliminados: {valores_nulos}\n")
    report.write(f"Registros finales: {num_registros_final}\n")

print("Proceso finalizado. Datos limpios guardados y reporte generado.")
