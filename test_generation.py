# test_generation.py
from etape6_generation import repondre

if __name__ == "__main__":
    question = "Comment poser un jour de congé ?"
    print(f"Question posée : '{question}'\n" + "-"*50)
    
    reponse, extraits = repondre(question, k=3)
    
    print("Réponse du LLM :\n")
    print(reponse)
    print("\n" + "-"*50)
    print("Sources utilisées :")
    for i, e in enumerate(extraits, 1):
        print(f"[{i}] {e['source']} (Page {e['page']} - Service: {e['service']})")