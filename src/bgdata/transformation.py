import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta

# Definir rutas de archivos
cleaned_path = "cleaned_data.csv"
additional_path = "src/bgdata/additional_data.csv"
enriched_path = "src/bgdata/enriched_data.csv"
audit_log_path = "src/bgdata/enrichment_report.txt"

# Función para generar datos adicionales si no existen
def generate_additional_data():
    if not os.path.exists(additional_path):
        print(f"El archivo {additional_path} no existe. Generando datos adicionales...")
        
        num_records = 100  # Ajustar según necesidad
        ids = np.arange(1, num_records + 1)
        prices = np.random.uniform(5, 50, num_records).round(2)
        start_date = datetime(2014, 1, 1)
        release_dates = [start_date + timedelta(days=30 * np.random.randint(0, 120)) for _ in range(num_records)]
        stock = np.random.randint(0, 101, num_records)

        additional_data = pd.DataFrame({
            "id": ids,
            "price": prices,
            "release_date": [d.strftime("%Y-%m-%d") for d in release_dates],
            "stock": stock
        })

        additional_data.to_csv(additional_path, index=False)
        print(f"Archivo {additional_path} generado con éxito.")

# Función para cargar datasets
def load_data():
    df_cleaned = pd.read_csv(cleaned_path)
    df_additional = pd.read_csv(additional_path)
    return df_cleaned, df_additional

# Función para enriquecer los datos
def enrich_data(df_cleaned, df_additional):
    enriched_df = df_cleaned.merge(df_additional, on="id", how="left")
    return enriched_df

# Función para generar archivo de auditoría
def generate_audit_log(df_cleaned, df_enriched):
    with open(audit_log_path, "w") as f:
        f.write("📊 Reporte de Enriquecimiento de Datos\n")
        f.write("="*50 + "\n")
        f.write(f"Registros en dataset base: {len(df_cleaned)}\n")
        f.write(f"Registros en dataset enriquecido: {len(df_enriched)}\n")
        f.write(f"Columnas añadidas: {list(set(df_enriched.columns) - set(df_cleaned.columns))}\n")
        f.write("Enriquecimiento completado exitosamente.\n")

# Función principal
def main():
    generate_additional_data()
    df_cleaned, df_additional = load_data()
    df_enriched = enrich_data(df_cleaned, df_additional)
    
    # Guardar dataset enriquecido
    df_enriched.to_csv(enriched_path, index=False)
    print(f"Archivo {enriched_path} guardado con éxito.")

    # Generar auditoría
    generate_audit_log(df_cleaned, df_enriched)
    print(f"Archivo de auditoría {audit_log_path} generado.")

if __name__ == "__main__":
    main()
