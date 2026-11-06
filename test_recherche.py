# test_recherche.py
from sentence_transformers import SentenceTransformer
import chromadb

# 1. Charger le modèle et se connecter à la base ChromaDB
modele = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
client = chromadb.PersistentClient(path="base_vectorielle")
collection = client.get_collection(name="altea")

# 2. Les 3 questions de salariés
questions = [
    "Combien de jours de télétravail ?",
    "Comment poser un jour de congé ?",
    "Quels sont les avantages des tickets restaurant ?"
]

# 3. Recherche et affichage pour chaque question
for idx, q in enumerate(questions, 1):
    print(f"\n{'='*50}")
    print(f"Q11 - Question {idx} : \"{q}\"")
    print(f"{'='*50}")
    
    resultat = collection.query(
        query_embeddings=modele.encode([q]).tolist(),
        n_results=3
    )
    
    documents = resultat["documents"][0]
    metadatas = resultat["metadatas"][0]
    distances = resultat["distances"][0]
    
    for i in range(len(documents)):
        print(f"\n  -> Chunk {i+1} (Distance: {distances[i]:.4f})")
        print(f"     Source : {metadatas[i].get('source')} (Page {metadatas[i].get('page')})")
        print(f"     Extrait : {documents[i][:150]}...")