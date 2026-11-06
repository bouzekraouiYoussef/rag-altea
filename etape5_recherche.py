# etape5_recherche.py
from sentence_transformers import SentenceTransformer
import chromadb

def rechercher(question, k=3):
    # Charger le modèle et la base
    modele = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
    client = chromadb.PersistentClient(path="base_vectorielle")
    collection = client.get_collection(name="altea")
    
    # Interroger ChromaDB
    resultat = collection.query(
        query_embeddings=modele.encode([question]).tolist(),
        n_results=k
    )
    
    # Formater les résultats sous forme de liste de dictionnaires
    chunks_trouves = []
    documents = resultat["documents"][0]
    metadatas = resultat["metadatas"][0]
    distances = resultat["distances"][0]
    
    for doc, meta, dist in zip(documents, metadatas, distances):
        chunks_trouves.append({
            "texte": doc,
            "source": meta.get("source"),
            "page": meta.get("page"),
            "service": meta.get("service"),
            "score": dist  # Plus la distance est faible, plus c'est proche
        })
        
    return chunks_trouves