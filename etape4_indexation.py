# etape4_indexation.py
import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
os.environ["MKL_NUM_THREADS"] = "1"
os.environ["VECLIB_MAXIMUM_THREADS"] = "1"
os.environ["NUMEXPR_NUM_THREADS"] = "1"

from sentence_transformers import SentenceTransformer
import chromadb
from etape1_collecte import collecter
from etape2_nettoyage import nettoyer
from etape3_decoupage import decouper_pages

# 1. Chargement du modèle d'embedding
modele = SentenceTransformer(
    "paraphrase-multilingual-MiniLM-L12-v2",
    model_kwargs={"low_cpu_mem_usage": False}
)

# 2. Connexion à ChromaDB
client = chromadb.PersistentClient(path="base_vectorielle")

# Nettoyage de l'ancienne collection pour repartir sur une base propre (évite les doublons)
try:
    client.delete_collection(name="altea")
except Exception:
    pass

collection = client.create_collection(
    name="altea",
    metadata={"hnsw:space": "cosine"}
)

# 3. Enchaînement des étapes 1 à 3 (Collecte, Nettoyage, Découpage)
pages = collecter()
for p in pages:
    p["texte"] = nettoyer(p["texte"])
pages = [p for p in pages if p["texte"]]  # Supprime les pages vides

chunks = decouper_pages(pages, taille=500, chevauchement=50)
nb_chunks_produits = len(chunks)
print(f"[Étape 3] Nombre de chunks produits : {nb_chunks_produits}")

# 4. Étape 4 : Vectorisation et Indexation dans ChromaDB
textes = [c["texte"] for c in chunks]
vecteurs = modele.encode(textes, batch_size=4, show_progress_bar=True).tolist()

collection.upsert(
    ids=[c["id"] for c in chunks],
    documents=textes,
    embeddings=vecteurs,
    metadatas=[
    {
        "source": c.get("source", "inconnue"), 
        "page": c.get("numero", c.get("page", 1)), 
        "service": c.get("service", "general")
    } 
    for c in chunks
]
)

print(f"[Étape 4] {collection.count()} chunks indexés avec succès.")