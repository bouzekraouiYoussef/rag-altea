# etape1_collecte.py
from pathlib import Path
from pypdf import PdfReader

def lire_pdf(chemin):
    lecteur = PdfReader(chemin)
    pages = []
    for numero, page in enumerate(lecteur.pages, start=1):
        texte = page.extract_text()
        pages.append({"source": chemin.name, "numero": numero, "texte": texte})
    return pages

def lire_txt(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        texte = f.read()
    return [{"source": chemin.name, "numero": 1, "texte": texte}]

def collecter(dossier="docs"):
    pages = []
    for chemin in sorted(Path(dossier).rglob("*")):
        if chemin.is_file():
            service = chemin.parent.name
            
            if chemin.suffix.lower() == ".pdf":
                docs_pages = lire_pdf(chemin)
            elif chemin.suffix.lower() == ".txt":
                docs_pages = lire_txt(chemin)
            else:
                continue
                
            for p in docs_pages:
                p["service"] = service
                pages.append(p)
                
    return pages