# test_nettoyage.py
from etape1_collecte import collecter
from etape2_nettoyage import nettoyer

def tester_nettoyage():
    print("=" * 55)
    print("TEST DE NETTOYAGE DU CORPUS - ALTÉA SERVICES")
    print("=" * 55)
    
    # 1. Collecte des pages brutes (Étape 1)
    pages_brutes = collecter()
    print(f"Nombre de pages avant nettoyage : {len(pages_brutes)}")
    
    # 2. Application du nettoyage à toutes les pages et suppression des pages vides (Q3)
    pages_nettoyees = []
    for p in pages_brutes:
        texte_propre = nettoyer(p["texte"])
        
        # On ne conserve la page que si elle contient encore du texte après nettoyage
        if texte_propre:
            p_copie = p.copy()
            p_copie["texte"] = texte_propre
            pages_nettoyees.append(p_copie)
            
    print(f"Nombre de pages après nettoyage et suppression des vides : {len(pages_nettoyees)}")
    
    # 3. Affichage d'un exemple pour vérifier (Q4)
    if pages_nettoyees:
        print("\n--- Exemple d'une page nettoyée ---")
        print(f"Source : {pages_nettoyees[0]['source']} (Page {pages_nettoyees[0]['numero']})")
        print(pages_nettoyees[0]["texte"][:300] + "...")
        
    print("=" * 55)

if __name__ == "__main__":
    tester_nettoyage()