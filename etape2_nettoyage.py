# etape2_nettoyage.py
import re

def nettoyer(texte):
    texte = re.sub(r"[ \t]+", " ", texte)  # plusieurs espaces -> un seul
    texte = re.sub(r"\n{3,}", "\n\n", texte) # remplacer 3 sauts de ligne ou plus par 2
    texte = re.sub(r"-\n(\w)", r"\1", texte) # recoller les mots coupés en fin de ligne
    return texte.strip()