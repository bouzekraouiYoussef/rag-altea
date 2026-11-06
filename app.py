# app.py
import streamlit as st
from etape6_generation import repondre

# Configuration de la page Streamlit
st.set_page_config(
    page_title="Assistant RAG - Altéa Services",
    page_icon="🤖",
    layout="centered"
)

st.title("💬 Assistant RH & Administratif - Altéa Services")
st.markdown("Posez vos questions sur la documentation interne de l'entreprise (congés, télétravail, frais, etc.).")

# Zone de saisie pour la question de l'utilisateur
question = st.text_input("Votre question :", placeholder="Ex : Comment poser un jour de congé ?")

# Bouton de validation
if st.button("Envoyer", type="primary"):
    if question.strip() == "":
        st.warning("Veuillez saisir une question valide.")
    else:
        with st.spinner("Recherche et génération de la réponse en cours..."):
            # Appel de la fonction de génération du RAG (avec k=3)
            reponse, extraits = repondre(question, k=3)
        
        # Affichage de la réponse du LLM
        st.subheader("Réponse :")
        st.write(reponse)
        
        # Affichage des sources mobilisées
        st.markdown("---")
        st.subheader("📚 Sources documentaires utilisées :")
        if extraits:
            for i, e in enumerate(extraits, 1):
                with st.expander(f"Extrait [{i}] - Fichier : {e['source']} (Page {e['page']}) | Service : {e.get('service', 'N/A')}"):
                    st.write(e['texte'])
        else:
            st.info("Aucune source trouvée pour cette question.")