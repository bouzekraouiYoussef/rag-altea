# etape7_evaluation.py
import csv
import os
from etape5_recherche import rechercher

def taux_reussite(fichier="evaluation.csv", k=3):
    """
    Calcule le taux de réussite (Recall@k) du système de recherche.
    Vérifie si le document attendu figure parmi les k premiers résultats trouvés.
    """
    if not os.path.exists(fichier):
        print(f"Erreur : Le fichier d'évaluation '{fichier}' est introuvable.")
        return 0.0

    with open(fichier, mode="r", encoding="utf-8") as f:
        lignes = list(csv.DictReader(f))
        
        if not lignes:
            print("Erreur : Le fichier d'évaluation est vide.")
            return 0.0

        trouves = 0
        for ligne in lignes:
            # Récupération des k extraits les plus pertinents via ChromaDB
            extraits = rechercher(ligne["question"], k=k)
            sources = [e["source"] for e in extraits]
            
            # Vérification : le document attendu est-il dans les sources retournées ?
            if ligne["document_attendu"] in sources:
                trouves += 1
                
        return trouves / len(lignes)


if __name__ == "__main__":
    print("=" * 55)
    print("ÉVALUATION DU RETRIEVER ALTÉA SERVICES (Recall@k)")
    print("=" * 55)
    
    for k in (1, 3, 5):
        score = taux_reussite(k=k) * 100
        print(f"k = {k} : {score:.0f}% des questions trouvent le bon document")
        
    print("=" * 55)