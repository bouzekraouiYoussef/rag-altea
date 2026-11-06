# test_q5.py
from etape6_generation import repondre

if __name__ == "__main__":
    # Liste de 5 questions : 3 couvertes par la doc et 2 sans rapport / sans réponse
    questions_test = [
        "Comment poser un jour de congé ?",                          # Réponse présente
        "Quel temps fera-t-il demain ?",                            # Sans réponse dans la doc
        "Quels sont les avantages des tickets restaurant ?",        # Réponse présente
        "Quelle est la recette de la tarte aux pommes de grand-mère ?", # Sans réponse dans la doc
        "Quelle est la politique de remboursement des frais ?"      # Réponse présente
    ]
    
    print("=" * 70)
    print("Q5 : TEST DE GÉNÉRATION SUR 5 QUESTIONS (AVEC ET SANS RÉPONSE)")
    print("=" * 70)
    
    for idx, question in enumerate(questions_test, 1):
        print(f"\n[Question {idx}] : \"{question}\"")
        print("-" * 70)
        
        # Appel de la fonction de génération
        reponse, extraits = repondre(question, k=3)
        
        print(f"RÉPONSE DU LLM :\n{reponse}\n")
        print("Sources mobilisées :")
        if extraits:
            for e in extraits:
                print(f"  - {e['source']} (Page {e['page']})")
        else:
            print("  - Aucune source pertinente trouvée.")
        print("=" * 70)