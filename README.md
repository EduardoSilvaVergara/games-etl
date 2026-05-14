# 🎮 Games ETL Pipeline

Pipeline ETL desarrollado en Python para procesar un dataset de videojuegos utilizando una arquitectura modular de Data Engineering.

El proyecto realiza:

* Ingesta de datos desde un archivo CSV
* Limpieza de datos
* Transformación de datos
* Validación estructural y semántica
* Carga automática a PostgreSQL en Neon
* Automatización mediante GitHub Actions

---

# 📌 Objetivo del proyecto

Construir un pipeline ETL automatizado capaz de:

1. Extraer datos desde un archivo CSV
2. Garantizar calidad e integridad de los datos
3. Transformar la información para análisis posteriores
4. Persistir los datos en una base de datos cloud
5. Automatizar el proceso usando CI/CD

---

# 🏗️ Arquitectura del pipeline

```txt
games.csv
   ↓
INGESTA
   ↓
VALIDACIÓN ESTRUCTURAL
   ↓
LIMPIEZA
   ↓
TRANSFORMACIÓN
   ↓
VALIDACIÓN SEMÁNTICA
   ↓
LOAD
   ↓
NEON POSTGRESQL
```

---

# 📂 Estructura del proyecto

```txt
games-etl/
│
├── .github/
│   └── workflows/
│       └── etl_pipeline.yml
│
├── data/
│   ├── games.csv
│   └── games_cleaned.csv
│
├── src/
│   ├── ingest.py
│   ├── clean.py
│   ├── transform.py
│   ├── validate.py
│   ├── load.py
│   └── main.py
│
├── requirements.txt
├── .gitignore
├── .env
└── README.md
```

---

# ⚙️ Tecnologías utilizadas

| Tecnología     | Uso                                     |
| -------------- | --------------------------------------- |
| Python         | Desarrollo del pipeline                 |
| Pandas         | Procesamiento y transformación de datos |
| PostgreSQL     | Base de datos relacional                |
| Neon           | Base de datos PostgreSQL cloud          |
| SQLAlchemy     | Conexión entre Python y PostgreSQL      |
| Git            | Control de versiones                    |
| GitHub         | Repositorio remoto                      |
| GitHub Actions | Automatización CI/CD                    |

---

# 📥 Tipo de ingesta

El proyecto implementa una:

## Ingesta Batch basada en archivos CSV

Características:

* Procesamiento por lotes
* Carga completa del archivo
* Datos estructurados
* Pipeline automatizado
* Full Load hacia PostgreSQL

El dataset completo es leído, procesado y cargado en cada ejecución del pipeline.

Además, el pipeline genera automáticamente un archivo `games_cleaned.csv` con los datos limpios y transformados.

---

# 🧹 Limpieza de datos

La etapa de limpieza realiza:

## Eliminación de duplicados

Se eliminan registros repetidos para evitar inconsistencias.

## Limpieza de texto

Se eliminan espacios innecesarios en columnas de texto:

* Title
* Team
* Genres
* Summary
* Reviews

## Conversión de tipos

Las columnas numéricas son convertidas correctamente utilizando Pandas.

## Manejo de valores nulos

Los valores faltantes son reemplazados por la mediana de cada columna numérica.

## Conversión de fechas

La columna `Release Date` es transformada al tipo datetime.

---

# 🔄 Transformación de datos

Durante la transformación se crean nuevas variables derivadas.

## Release Year

Extrae el año de lanzamiento del videojuego.

## Popularity Score

Métrica calculada mediante:

```txt
Plays + Playing + Wishlist
```

Permite medir la popularidad total de cada juego.

## Rating Category

Clasificación del rating:

| Rating | Categoría |
| ------ | --------- |
| 8 - 10 | Excelente |
| 6 - 7  | Bueno     |
| 4 - 5  | Regular   |
| 0 - 3  | Malo      |

---

# ✅ Validaciones implementadas

## Validación estructural

Verifica:

* Existencia de columnas obligatorias
* Integridad del esquema
* Compatibilidad del dataset

## Validación semántica

Verifica:

* Ratings válidos
* Ausencia de valores negativos
* Títulos no vacíos
* Consistencia lógica de los datos

---

# 💾 Exportación de datos limpios

Después de la limpieza y transformación, el pipeline genera automáticamente:

```txt
data/games_cleaned.csv
```

Este archivo contiene:

* Datos limpios
* Tipos corregidos
* Fechas transformadas
* Valores nulos tratados
* Nuevas columnas derivadas
* Métricas de popularidad

El CSV limpio puede utilizarse para:

* Power BI
* Machine Learning
* Dashboards
* Análisis exploratorio
* Auditoría de datos

---

# ☁️ Base de datos

El pipeline utiliza PostgreSQL en Neon.

## Razones de la elección

* Base de datos cloud
* Escalable
* Compatible con Python
* Integración sencilla con GitHub Actions
* Ideal para proyectos ETL y análisis de datos

---

# 🗑️ Gestión automática de tablas en Neon

Antes de cargar los nuevos datos, el pipeline ejecuta:

```sql
DROP TABLE IF EXISTS games
```

Esto permite:

* Evitar duplicados
* Reemplazar esquemas antiguos
* Mantener consistencia de datos
* Garantizar cargas limpias

Posteriormente la tabla es recreada automáticamente usando Pandas y SQLAlchemy.

---

# 🚀 Automatización con GitHub Actions

El proyecto incorpora CI/CD mediante GitHub Actions.

Cada vez que se realiza un:

```bash
git push
```

El workflow:

1. Clona el repositorio
2. Instala Python
3. Instala dependencias
4. Ejecuta el pipeline ETL
5. Carga automáticamente los datos a Neon

---

# 🔐 Variables de entorno

El proyecto utiliza un archivo `.env` para proteger credenciales.

Ejemplo:

```env
DATABASE_URL=postgresql://usuario:password@host/database?sslmode=require
```

---

# 🧩 Extensión recomendada para VS Code

Se recomienda instalar la extensión:

```txt
CSV
```

Disponible en el Marketplace de Visual Studio Code.

Esta extensión permite:

* Visualizar CSV como tablas
* Filtrar columnas
* Ordenar datos
* Mejorar la lectura del dataset
* Analizar fácilmente `games.csv` y `games_cleaned.csv`

---

# 📦 Instalación

## 1. Clonar repositorio

```bash
git clone https://github.com/TU_USUARIO/games-etl.git
```

## 2. Entrar al proyecto

```bash
cd games-etl
```

## 3. Crear entorno virtual

```bash
python -m venv venv
```

## 4. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# ▶️ Ejecución del pipeline

```bash
python src/main.py
```

---

# 📊 Dataset utilizado

El dataset contiene información de videojuegos:

* Título
* Fecha de lanzamiento
* Rating
* Géneros
* Reviews
* Wishlist
* Plays
* Popularidad

---

# 📈 Posibles usos futuros

El proyecto puede extenderse para:

* Dashboards en Power BI
* Machine Learning
* APIs de videojuegos
* Análisis predictivo
* Sistemas de recomendación
* ETL incremental
* Streaming de datos

---

# 👨‍💻 Autor

Proyecto desarrollado como práctica de:

* Data Engineering
* ETL Pipelines
* Automatización de datos
* Integración Cloud
* CI/CD

---

# 📄 Licencia

Proyecto de uso académico y educativo.
