import os
import chromadb

def iniciar_sistema_vectorial():
    # Definimos la ruta de almacenamiento local para que persistan los datos.
    ruta_db = os.path.join(os.getcwd(), "chroma_data")
    
    # Inicializamos el cliente persistente.
    cliente = chromadb.PersistentClient(path=ruta_db)
    
    # Creamos o recuperamos la colección.
    coleccion = cliente.get_or_create_collection(name="ejercicio_practico")
    
    print("\n" +"=" *61)
    print(" PROGRAMA DE EJEMPLO DE USO DE CHROMA DB - SISTEMA VECTORIAL ")
    print("=" *61 + "\n")
    # Ingesta de datos de prueba estructurados.
    print("\n[INFO] Insertando documentos en el espacio vectorial...\n")

    coleccion.add(
        documents=[
            "Las bases de datos vectoriales indexan datos mediante embeddings matemáticos.",
            "MariaDB es un motor relacional basado en tablas SQL y álgebra relacional.",
            "Git es un sistema de control de versiones distribuido para rastrear cambios."
        ],
        metadatas=[{"categoria": "teoria"}, {"categoria": "bd"}, {"categoria": "versiones"}],
        ids=["id_001", "id_002", "id_003"]
    )
    
    # Simulación de consulta por similitud semántica.
    consulta = "Necesito almacenar embeddings de alta dimensionalidad\n"
    print(f"\n[CONSULTA] Buscando: '{consulta}'")
    
    resultado = coleccion.query(
        query_texts=[consulta],
        n_results=1
    )
    
    print(" RESULTADO MÁS CERCANO ")
    print("=" * 23 + "\n")
    print(f"Documento encontrado: {resultado['documents'][0][0]}")
    print(f"Metadatos: {resultado['metadatas'][0][0]}")
    print(f"Distancia matemática (menor es más cercano): {resultado['distances'][0][0]}")

if __name__ == "__main__":
    iniciar_sistema_vectorial()