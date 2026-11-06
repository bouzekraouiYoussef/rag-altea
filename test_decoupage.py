# test_decoupage.py
from etape1_collecte import collecter
from etape2_nettoyage import nettoyer
from etape3_decoupage import decouper_pages

def tester_decoupage_tailles():
    # Récupération et nettoyage du corpus
    pages = collecter()
    pages_propres = [{"source": p["source"], "numero": p["numero"], "service": p["service"], "texte": nettoyer(p["texte"])} for p in pages if nettoyer(p["texte"])]
    
    configurations = [
        (200, 20),
        (500, 50),
        (1000, 100)
    ]
    
    print("=" * 65)
    print(f"{'Taille':<10} | {'Chevauchement':<15} | {'Nb Chunks':<12} | {'Long. Moyenne'}")
    print("-" * 65)
    
    for taille, chevauchement in configurations:
        chunks = decouper_pages(pages_propres, taille=taille, chevauchement=chevauchement)
        nb_chunks = len(chunks)
        longueur_moyenne = sum(len(c["texte"]) for c in chunks) / nb_chunks if nb_chunks > 0 else 0
        
        print(f"{taille:<10} | {chevauchement:<15} | {nb_chunks:<12} | {longueur_moyenne:.1f}")
        
    print("=" * 65)

if __name__ == "__main__":
    tester_decoupage_tailles()