# etape7_evaluation.py
import csv
from etape5_recherche import rechercher

def taux_reussite(fichier="evaluation.csv", k=3):
    with open(fichier, encoding="utf-8") as f:
        lignes = list(csv.DictReader(f))
    
    trouves = 0
    for ligne in lignes:
        # Récupère les sources des k premiers chunks trouvés
        sources = [r["source"] for r in rechercher(ligne["question"], k)]
        
        doc_attendu = ligne["document_attendu"]
        
        # Gestion du cas où aucune réponse/document n'est attendu ("aucun")
        if doc_attendu == "aucun" and len(sources) == 0:
            trouves += 1
        # Gestion du cas classique : le document attendu est dans les sources remontées
        elif doc_attendu in sources:
            trouves += 1
            
    return trouves / len(lignes)

if __name__ == "__main__":
    print("=" * 60)
    print("LANCEMENT DE L'ÉVALUATION DU RAPPEL (RETRIEVAL)")
    print("=" * 60)
    
    # Test avec différentes valeurs de k (1, 3 et 5)
    for k in (1, 3, 5):
        taux = taux_reussite(fichier="evaluation.csv", k=k)
        print(f"k = {k} : {taux:.0%} de questions où le bon document est trouvé")