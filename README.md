# 🚀 TP N°8: Bases de Datos Vectoriales

**Institución:** Instituto Superior de Formación Técnica N° 151
**Carrera:** Tecnicatura Superior de Análisis de Sistemas
**Cátedra:** Base de Datos
**Tema:** Introducción a Bases de Datos Vectoriales
**Alumno:** David Hernán Bravo

---

## 🎯 Objetivo del Proyecto
Este repositorio contiene la investigación teórica y la implementación práctica sobre **Bases de Datos Vectoriales**. Pasamos del modelo relacional clásico (SQL) a un paradigma basado en **embeddings** y **búsqueda por similitud semántica** en espacios multidimensionales, tecnología fundamental para las arquitecturas modernas de IA (como RAG - *Retrieval-Augmented Generation*). 🧠⚙️

## 🛠️ Tecnologías y Herramientas
* **Lenguaje:** Python v3.14+ 🐍
* **Motor Vectorial:** ChromaDB (Open-source, ejecución local) 🗄️
* **Entorno:** Entorno virtual aislado (`.venv`)

## 🚀 Guía de Despliegue Local

### 1️⃣ Navegación al Directorio
Asegurate de estar en la carpeta correcta del repositorio. Usá comillas dobles si hay espacios en la ruta:

```bash
cd "D:\Repositorios de GitHub\ISFT N°151\Base de Datos\Trabajos Prácticos\TP_N8"
```

### 2️⃣ Creación y Activación del Entorno Virtual
Para no contaminar el entorno global del sistema operativo y mantener la portabilidad del proyecto:

python -m venv .venv

### Activación en CMD de Windows:

.\.venv\Scripts\activate.bat

### 3️⃣ Instalación de Dependencias
Actualizamos los empaquetadores (crítico por el uso de Python 3.14) e instalamos el motor vectorial:

python -m pip install --upgrade pip setuptools wheel
pip install chromadb

### 4️⃣ Ejecución de la Prueba de Concepto
El script app.py inicializa la base de datos persistente de forma local (en la carpeta chroma_data/), ingesta un lote de documentos de prueba y realiza una consulta semántica por proximidad geométrica.

python app.py

### 🖥️ Resultado Esperado en Consola
Al ejecutar el script, el sistema vectoriza los documentos y, ante la consulta "Necesito almacenar embeddings de alta dimensionalidad", devuelve el registro matemáticamente más cercano:

```bash
=============================================================
 PROGRAMA DE EJEMPLO DE USO DE CHROMA DB - SISTEMA VECTORIAL 
=============================================================

[INFO] Insertando documentos en el espacio vectorial...

[CONSULTA] Buscando: 'Necesito almacenar embeddings de alta dimensionalidad'

 RESULTADO MÁS CERCANO 
=======================

Documento encontrado: Las bases de datos vectoriales indexan datos mediante embeddings matemáticos.
Metadatos: {'categoria': 'teoria'}
Distancia matemática (menor es más cercano): 0.9008001685142517
```

### 🧹 Higiene del Repositorio: 
Los binarios de la base de datos embebida (chroma_data/) y los archivos del entorno virtual (.venv/) se excluyen explícitamente del control de versiones mediante el archivo .gitignore.

### 📚 Referencias

Amazon Web Services (AWS) - ¿Qué es una base de datos vectorial?

IBM - Bases de datos vectoriales

ChromaDB - Documentación Oficial

Medium - Vector Databases: A Beginner’s Guide