import streamlit as st
from stock import ajt_prd, sup_prd, mdf_qnt, aff_stock, stock
from stats import stats
from visualize import visualize_bar, visualize_pie

if "stock" not in st.session_state:
    st.session_state.stock = []
st.title("📦 Gestion du Stock avec Streamlit")

# Menu Streamlit
menu_options = [
    "Ajouter un produit",
    "Supprimer un produit",
    "Modifier la quantité d’un produit",
    "Afficher le stock",
    "Afficher les statistiques",
    "Afficher un graphique"
]

choice = st.sidebar.selectbox("Menu", menu_options)

# Utiliser le stock de la session
stock = st.session_state.stock

# ===== Ajouter un produit =====
if choice == "Ajouter un produit":
    prd_input = st.text_input("Entrez le produit (Nom,Quantité,Prix)")
    if st.button("Ajouter"):
        ajt_prd()
        aff_stock()

# ===== Supprimer un produit =====
elif choice == "Supprimer un produit":
    if stock:
        noms = [p[0] for p in stock]
        sel = st.selectbox("Sélectionnez un produit à supprimer", noms)
        if st.button("Supprimer"):
            sup_prd()
            aff_stock()
    else:
        st.info("Le stock est vide.")

# ===== Modifier quantité =====
elif choice == "Modifier la quantité d’un produit":
    if stock:
        noms = [p[0] for p in stock]
        sel = st.selectbox("Sélectionnez un produit à modifier", noms)
        nouvelle_qte = st.number_input("Nouvelle quantité", min_value=0, step=1)
        if st.button("Modifier"):
            mdf_qnt()
            aff_stock()
    else:
        st.info("Le stock est vide.")

# ===== Afficher le stock =====
elif choice == "Afficher le stock":
    aff_stock()

# ===== Statistiques =====
elif choice == "Afficher les statistiques":
    stats()

# ===== Graphiques =====
elif choice == "Afficher un graphique":
    chart_type = st.radio("Choisir le type de graphique", ["Bar chart", "Pie chart"])
    if chart_type == "Bar chart":
        visualize_bar()
    else:
        visualize_pie()
