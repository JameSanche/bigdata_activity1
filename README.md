## **📌 Proyecto de Ingesta y Limpieza de Datos - Big Data**  
Este proyecto implementa la etapa de ingesta y limpieza de datos como parte de un sistema Big Data. Se extraen datos desde una API, se almacenan en una base de datos SQLite, se realizan procesos de calidad y se generan archivos de evidencia para su validación.

---

## **🎯 Objetivos**  
✅ Obtener datos desde una API.  
✅ Almacenar los datos en una base de datos SQLite.  
✅ Identificar y corregir problemas de calidad en los datos.  
✅ Generar archivos de evidencia:  
   - CSV/Excel con los datos limpios.  
   - Archivo de auditoría con las transformaciones realizadas.  

---

## **📁 Estructura del Proyecto**  
```
bigdata_activity1/
│-- venv/                    # Entorno virtual de Python
│-- src/
│   ├── bgdata/
│   │   ├── actividad1.py    # Script de ingesta de datos
│   │   ├── cleaning.py      # Script de limpieza y transformación de datos
│-- databases/
│   ├── raw_data.db          # Base de datos original con datos sin procesar
│   ├── cleaned_data.db      # Base de datos con datos limpios y transformados
│-- evidencia/
│   ├── muestra_datos.csv    # Muestra de datos antes de la limpieza
│   ├── cleaned_data.csv     # Muestra de datos después de la limpieza
│   ├── muestra_datos.xlsx   # Muestra de datos antes de la limpieza (Excel)
│   ├── cleaned_data.xlsx    # Muestra de datos después de la limpieza (Excel)
│   ├── cleaning_report.txt  # Archivo de auditoría con las transformaciones
│-- README.md                # Documentación del proyecto
```

---

## **🚀 Requisitos**  

### **1️⃣ Instalación de dependencias**  
Este proyecto usa **Python 3.x**. Instala los paquetes requeridos con:  
```sh
pip install requests pandas openpyxl
```

### **2️⃣ Configuración del Entorno Virtual (Opcional, pero Recomendado)**  
```sh
python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate     # En Windows
```

---

## **⚙️ Ejecutar el Proyecto**  

### **1️⃣ Ingesta de Datos**  
Ejecuta el siguiente comando para extraer datos de la API y almacenarlos en `raw_data.db`:  
```sh
python src/bgdata/actividad1.py
```
Este script generará:
✅ Base de datos **raw_data.db** con los datos sin procesar.  
✅ Archivo CSV (`muestra_datos.csv`) y Excel (`muestra_datos.xlsx`).  
✅ Archivo de auditoría (`auditoria.txt`) que compara los datos extraídos con los almacenados.  

### **2️⃣ Limpieza y Transformación de Datos**  
Después de la ingesta, ejecuta el siguiente comando para limpiar los datos:  
```sh
python src/bgdata/cleaning.py
```
Este script:
✅ **Elimina duplicados y registros con valores en 0.**  
✅ **Maneja valores nulos mediante imputación o eliminación.**  
✅ **Corrige tipos de datos (conversión de cadenas a números o fechas).**  
✅ **Aplica transformaciones adicionales (normalización, escalado, etc.).**  
✅ **Genera la base de datos `cleaned_data.db` con los datos limpios.**  
✅ **Crea archivos de evidencia (`cleaned_data.csv` y `cleaning_report.txt`).**  

---

## **📊 Ejemplo de Datos Obtenidos y Limpiados**  

**Estructura de la Tabla en SQLite (`crypto_data`)**  
| ID  | High   | Low    | Vol  | Last  | Buy  | Sell  | Date       |
|----|--------|--------|------|------|------|------|------------|
| 1  | 50000  | 48000  | 100  | 49500 | 49400 | 49600 | 1700000000 |
| 2  | 52000  | 51000  | 150  | 51500 | 51450 | 51550 | 1700000050 |

---

## **📜 Archivo de Auditoría (`cleaning_report.txt`)**  
El archivo `cleaning_report.txt` documenta los procesos aplicados a los datos.  

### **Ejemplo de Auditoría**
```
📊 Proceso de Limpieza y Validación de Datos
==================================================
🔹 Registros antes de la limpieza: 10,000
🔹 Registros después de la limpieza: 9,800
--------------------------------------------------
🔹 Duplicados eliminados: 50
🔹 Registros con valores en 0 eliminados: 100
🔹 Valores nulos imputados: 30
🔹 Correcciones de tipo de datos aplicadas: Sí
--------------------------------------------------
✅ Datos limpios almacenados en cleaned_data.db
✅ Archivo de evidencia generado: cleaned_data.csv
```

Si hay diferencias significativas o problemas en los datos, estos se detallarán en el informe.

---

## **👥 Autores**  
📌 **Patricia Franco R**  
📌 **James Sanchez T**  

---

**Notas Finales:**  
✔️ Ahora el proyecto no solo ingesta datos, sino que también los limpia y los transforma antes de almacenarlos en la base de datos final.  

