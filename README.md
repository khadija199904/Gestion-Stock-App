# 🏪 Stock Manager  
## Description
Stock Manager est une application Python en ligne de commande permettant de gérer un stock de produits, d’effectuer des analyses statistiques et de visualiser les données à l’aide de NumPy et Matplotlib.

Ce projet est organisé en plusieurs modules pour assurer une structure claire, modulaire et facile à maintenir.

##  Structure du application 
Stock-Manager/
│
├── main.py              # Point d’entrée du programme (menu principal)
├── stock.py             # Fonctions de gestion du stock (ajout, suppression, mise à jour…)
├── stats.py             # Fonctions de calculs statistiques avec NumPy
├── visualize.py         # Fonctions de visualisation avec Matplotlib
├── menu.py              # Menu interactif en console

##  Fonctionnalités principales

-  **Ajouter** un produit au stock
-  **Supprimer** un produit
-  **Mettre à jour** les informations d’un produit
-  **Calculer des statistiques** (moyenne, somme, min, max, etc.) avec **NumPy**
-  **Visualiser les données** (graphique des ventes, répartition des stocks, etc.) avec **Matplotlib**
-  **Interface console interactive** (menu simple et intuitif)
-  
### Contributions possibles
- Ajouter la gestion des utilisateurs avec authentification.   
- Améliorer les visualisations avec des graphiques interactifs (ex. Plotly, Seaborn).  
- Ajouter un export/import de données au format CSV ou Excel.  

### Perspectives d’évolution
- Déploiement de l’application en interface web avec Streamlit ou Flask.  
- Mise en place d’un système d’alertes pour les stocks faibles ou produits périmés.  
- Intégration d’un module de rapports automatiques (PDF, Excel) pour la gestion du stock.

  ## Installation

1. Cloner le dépôt :
```bash
git clone https://github.com/votre-utilisateur/Gestion-stock-app.git
cd Gestion-stock-app/src
```
2. Installer les dépendances :
```bash
pip install -r requirements.txt
```
3. Lancer l'application :
```bash
  python main.py
```







