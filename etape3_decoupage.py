# etape3_decoupage.py

def decouper(texte, taille=500, chevauchement=50):
    assert chevauchement < taille, "Le chevauchement doit être plus petit que la taille"
    morceaux = []
    debut = 0
    while debut < len(texte):
        fin = min(debut + taille, len(texte))
        morceaux.append(texte[debut:fin])
        if fin >= len(texte):
            break
        debut += taille - chevauchement
    return morceaux

def decouper_pages(pages, taille=500, chevauchement=50):
    tous_les_chunks = []
    for p in pages:
        morceaux = decouper(p["texte"], taille, chevauchement)
        for i, texte_chunk in enumerate(morceaux):
            chunk = {
                # Correction ici : on utilise p["numero"] au lieu de p["page"]
                "id": f"{p['source']}-p{p['numero']}-{i}",
                "texte": texte_chunk,
                "source": p["source"],
                "numero": p["numero"],
                "service": p.get("service", "General")
            }
            tous_les_chunks.append(chunk)
    return tous_les_chunks