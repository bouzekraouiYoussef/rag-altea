# test_collecte.py
from etape1_collecte import collecter

def lancer_test_collecte():
    print("=" * 55)
    print("TEST DE COLLECTE DES DOCUMENTS - ALTÉA SERVICES")
    print("=" * 55)
    
    pages = collecter()
    print(f"Nombre total de pages lues : {len(pages)}")
    
    # Comptage des pages lues pour chaque document
    compteur_docs = {}
    for p in pages:
        src = p["source"]
        compteur_docs[src] = compteur_docs.get(src, 0) + 1
        
    print("\nNombre de pages lues pour chaque document :")
    for doc, nb_pages in compteur_docs.items():
        print(f"- {doc} : {nb_pages} page(s)")
        
    print("=" * 55)

if __name__ == "__main__":
    lancer_test_collecte()