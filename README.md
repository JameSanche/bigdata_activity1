# Proyecto de Ingesta de Datos - Big Data

Este proyecto implementa la **etapa de ingesta de datos** como parte de un sistema Big Data. Se extraen datos desde una API, se almacenan en una base de datos SQLite y se generan archivos de evidencia para su validación.

## 📌 **Objetivos**
- Obtener datos desde una API.
- Almacenar los datos en una base de datos **SQLite**.
- Generar archivos de evidencia:
  - **CSV/Excel** con una muestra de los datos.
  - **Archivo de auditoría** que compara los datos extraídos con los almacenados.

## 📁 **Estructura del Proyecto**
```
bigdata_activity1/
│-- venv/                    # Entorno virtual de Python
│-- src/
│   ├── bgdata/
│   │   ├── actividad1.py    # Script principal
│-- big_data.db               # Base de datos SQLite (se genera tras ejecutar el script)
│-- muestra_datos.csv         # Archivo CSV con una muestra de los datos
│-- muestra_datos.xlsx        # Archivo Excel con una muestra de los datos
│-- auditoria.txt             # Archivo de auditoría con la comparación de datos
│-- README.md                 # Documentación del proyecto
```

## 🚀 **Requisitos**
### 1️⃣ Instalación de dependencias
Este proyecto usa **Python 3.x**. Instala los paquetes requeridos con:
```bash
pip install requests pandas openpyxl
```

### 2️⃣ Configuración del Entorno Virtual *(opcional pero recomendado)*
```bash
python -m venv venv
source venv/bin/activate  # En Mac/Linux
venv\Scripts\activate     # En Windows
```

## ⚙️ **Ejecutar el Script**
Corre el siguiente comando en la terminal dentro del directorio del proyecto:
```bash
python src/bgdata/actividad1.py
```
Esto generará:
- **Base de datos SQLite (`big_data.db`)** con los datos extraídos.
- **Archivo CSV (`muestra_datos.csv`) y Excel (`muestra_datos.xlsx`)**.
- **Archivo de auditoría (`auditoria.txt`)** que compara los datos extraídos con los almacenados.

## 📊 **Ejemplo de Datos Obtenidos**
Los datos obtenidos de la API se almacenan en la tabla **crypto_data** de SQLite y tienen la siguiente estructura:

| ID | High | Low | Vol | Last | Buy | Sell | Date |
|----|------|-----|-----|------|-----|------|------|
| 1  | 50000 | 48000 | 100 | 49500 | 49400 | 49600 | 1700000000 |

## 📜 **Archivo de Auditoría**
El archivo `auditoria.txt` muestra si hay diferencias entre los datos extraídos y los almacenados en la base de datos. Ejemplo:
```
📊 Comparación de datos entre API y Base de Datos
==================================================
✅ No se encontraron diferencias entre los datos del API y la base de datos.
```

Si hay diferencias, se detallarán en el archivo.


## Patricia Franco R ---- James Sanchez T

---


