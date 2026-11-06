# etape5_recherche.py
from sentence_transformers import SentenceTransformer
import chromadb

def rechercher(requete, k=3):
    # Charger le modèle d'embedding
    modele = SentenceTransformer(
        "paraphrase-multilingual-MiniLM-L12-v2",
        model_kwargs={"low_cpu_mem_usage": False}
    )
    
    # Connexion à la base ChromaDB existante
    client = chromadb.PersistentClient(path="base_vectorielle")
    collection = client.get_collection(name="altea")
    
    # Vectorisation de la requête
    vecteur_requete = modele.encode(requete).tolist()
    
    # Interrogation de la base
    reponses = collection.query(
        query_embeddings=[vecteur_requete],
        n_results=k
    )
    
    resultats_formes = []
    for doc, metadata, distance in zip(
        reponses['documents'][0], 
        reponses['metadatas'][0], 
        reponses['distances'][0]
    ):
        resultats_formes.append({
            "texte": doc,
            "source": metadata.get("source"),
            "page": metadata.get("page", metadata.get("numero", "N/A")), # gère 'page' ou 'numero'
            "service": metadata.get("service"),
            "score": distance
        })
        
    return resultats_formes