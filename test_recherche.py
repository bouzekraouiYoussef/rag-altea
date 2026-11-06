# test_recherche_q1.py
from etape5_recherche import rechercher

if __name__ == "__main__":
    questions = [
        "Comment poser un jour de congé ?",
        "Quels sont les avantages des tickets restaurant ?",
        "Quelle est la politique de télétravail ?"
    ]
    
    for idx, q in enumerate(questions, 1):
        print(f"\n{'='*60}")
        print(f" Question {idx} : \"{q}\"")
        print(f"{'='*60}")
        
        resultats = rechercher(q, k=3)
        for i, r in enumerate(resultats, 1):
            print(f"  -> Résultat {i} | Score (distance) : {r['score']:.4f}")
            print(f"     Source : {r['source']} (Page {r['page']} | Service : {r['service']})")
            print(f"     Extrait : {r['texte'][:150]}...")
            print()