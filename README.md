# 🤖 Assistant RAG - Altéa Services

## 🎯 Objectif du projet
Ce projet consiste à développer un système de **Génération Augmentée par Récupération (RAG)** pour Altéa Services. L'objectif est de permettre aux salariés d'interroger la documentation interne de l'entreprise (frais professionnels, congés, télétravail, mutuelle) de manière fiable, rapide et traçable grâce à un grand modèle de langage (LLM) couplé à une base vectorielle ChromaDB.

## 📦 Installation

1. **Cloner le dépôt Git :**
   ```bash
   git clone https://github.com/bouzekraouiYoussef/rag-altea.git
   cd rag-altea
   ```

2. **Créer et activer l'environnement virtuel (sur Windows) :**
   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate
   ```

3. **Installer les dépendances requises :**
   ```powershell
   pip install -r requirements.txt
   ```

## 🚀 Ordre de lancement des scripts

Exécutez les scripts dans l'ordre suivant pour initialiser, évaluer et lancer l'application :

1. **Indexation des documents dans la base vectorielle :**
   ```powershell
   python etape4_indexation.py
   ```
2. **Test de la recherche vectorielle (Retrieval) :**
   ```powershell
   python etape5_recherche.py
   ```
3. **Évaluation automatique du taux de rappel (*Retrieval Recall*) :**
   ```powershell
   python etape7_evaluation.py
   ```
4. **Lancement de l'interface utilisateur web Streamlit :**
   ```powershell
   streamlit run app.py
   ```

## 💡 Exemple de question
* **Question posée :** « Comment poser un jour de congé ? »
* **Source identifiée :** `conges.pdf`
* **Réponse attendue :** Explication détaillée de la procédure d'imputation sur le portail RH avec mention explicite du document source officiel.

## 📊 Résultats de l'étape 7 (Évaluation)
L'évaluation réalisée sur le jeu de données `evaluation.csv` (10 questions de test) confirme l'efficacité du système de recherche selon la valeur du paramètre $k$ :
* **Taux de rappel pour $k=1$ :** 70% des bons documents retrouvés.
* **Taux de rappel pour $k=3$ :** 90% des bons documents retrouvés.
* **Taux de rappel pour $k=5$ :** 100% des bons documents retrouvés en tête de liste.

## ⚠️ Limites connues
* **Sensibilité au découpage (*Chunking*) :** Si une information clé est découpée à cheval sur deux blocs de texte, le LLM peut perdre une partie du contexte.
* **Absence de contrôle d'accès (RBAC) :** Le prototype actuel ne restreint pas l'accès aux documents selon le profil ou le service du salarié connecté.

## 👥 Auteurs
* **Bouzekraoui Youssef** - Altéa Services