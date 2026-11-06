# etape6_generation.py
from openai import OpenAI
from etape5_recherche import rechercher

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)
MODELE = "llama3.2"
REPLI = "Je ne trouve pas cette information dans la documentation."

def construire_prompt(question, extraits):
    contexte = ""
    for i, e in enumerate(extraits, start=1):
        contexte += f"[{i}] ({e['source']}, page {e['page']})\n{e['texte']}\n\n"
    
    return f"""Tu es l'assistant interne d'Altéa Services.
Réponds à la question en utilisant UNIQUEMENT les extraits ci-dessous.
Après chaque information, indique le numéro de l'extrait entre crochets, par exemple [1].
Si les extraits ne contiennent pas la réponse, réponds exactement : "{REPLI}"

Extraits :
{contexte}

Question : {question}
Réponse : """

def repondre(question, k=3):
    extraits = rechercher(question, k)
    prompt = construire_prompt(question, extraits)
    
    # ON FORCE ICI num_gpu=0 directement dans la requête pour bypasser le GPU !
    reponse = client.chat.completions.create(
        model=MODELE,
        messages=[{"role": "user", "content": prompt}],
        temperature=0,
        extra_body={"options": {"num_gpu": 0}} 
    )
    return reponse.choices[0].message.content, extraits