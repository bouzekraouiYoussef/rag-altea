# test_evaluation.py
from etape7_evaluation import taux_reussite

def lancer_evaluation():
    print("=" * 55)
    print("TEST D'ÉVALUATION DU PIPELINE RAG - ALTÉA SERVICES")
    print("=" * 55)
    
    valeurs_k = [1, 3, 5]
    
    for k in valeurs_k:
        score = taux_reussite(fichier="evaluation.csv", k=k)
        pourcentage = score * 100
        print(f"Recall@{k} : {pourcentage:.1f}% de réussite")
    
    print("=" * 55)

if __name__ == "__main__":
    lancer_evaluation()