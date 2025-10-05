import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ========= STOCK GLOBAL =========
if "stock" not in st.session_state:
    st.session_state.stock = []

# ========= FONCTIONS ADAPTÉES POUR STREAMLIT =========
def ajt_prd_streamlit(stock, prd_input):
    try:
        nom, qnt, prix = prd_input.split(",")
        stock.append([nom.strip(), int(qnt), float(prix)])
        st.success(f"✅ {nom.strip()} ajouté au stock.")
    except ValueError:
        st.error("⚠️ Format invalide. Exemple : ProduitA,10,15.5")

def sup_prd_streamlit(stock, nom):
    for p in stock:
        if p[0] == nom:
            stock.remove(p)
            st.warning(f"🗑️ {nom} supprimé du stock.")
            return
    st.error("❌ Produit introuvable.")

def mdf_qnt_streamlit(stock, nom, nouvelle_qte):
    for p in stock:
        if p[0] == nom:
            p[1] = nouvelle_qte
            st.info(f"🔄 Quantité de {nom} mise à jour à {nouvelle_qte}.")
            return
    st.error("❌ Produit introuvable.")

def aff_stock_streamlit(stock):
    if not stock:
        st.info("📦 Le stock est vide.")
    else:
        st.subheader("📋 Stock actuel :")
        for p in stock:
            st.write(f"- {p[0]} : quantité = {p[1]}, prix = {p[2]} DH")

def stats_streamlit(stock):
    if not stock:
        st.info("📦 Le stock est vide.")
        return

    Qnt = np.array([p[1] for p in stock])
    Prix = np.array([p[2] for p in stock])
    Total = sum(Qnt * Prix)
    Moy = np.mean(Prix)
    Total_articles = sum(Qnt)

    st.subheader("📊 Statistiques du stock")
    st.write(f"Nombre total d'articles : **{Total_articles}**")
    st.write(f"Valeur totale du stock : **{Total:.2f} DH**")
    st.write(f"Prix moyen unitaire : **{Moy:.2f} DH**")

def visualize_bar_streamlit(stock):
    if not stock:
        st.info("📦 Le stock est vide.")
        return

    produits = [p[0] for p in stock]
    valeurs = [p[1] * p[2] for p in stock]
    fig, ax = plt.subplots()
    ax.bar(produits, valeurs, color='skyblue')
    ax.set_xlabel("Produits")
    ax.set_ylabel("Valeur totale (DH)")
    ax.set_title("Valeur du stock par produit")
    st.pyplot(fig)

def visualize_pie_streamlit(stock):
    if not stock:
        st.info("📦 Le stock est vide.")
        return

    produits = [p[0] for p in stock]
    valeurs = [p[1] * p[2] for p in stock]
    fig, ax = plt.subplots()
    ax.pie(valeurs, labels=produits, autopct="%1.1f%%", startangle=90)
    ax.set_title("Répartition de la valeur du stock")
    st.pyplot(fig)

# ========= INTERFACE STREAMLIT =========
st.title("📦 Application de Gestion du Stock")

menu = [
    "Ajouter un produit",
    "Supprimer un produit",
    "Modifier la quantité d’un produit",
    "Afficher le stock",
    "Afficher les statistiques",
    "Afficher un graphique"
]
choix = st.sidebar.selectbox("Menu", menu)
stock = st.session_state.stock

# ----- Ajouter -----
if choix == "Ajouter un produit":
    prd_input = st.text_input("Entrez le produit (Nom,Quantité,Prix)")
    if st.button("Ajouter au stock"):
        ajt_prd_streamlit(stock, prd_input)
    aff_stock_streamlit(stock)

# ----- Supprimer -----
elif choix == "Supprimer un produit":
    if stock:
        noms = [p[0] for p in stock]
        nom_sel = st.selectbox("Sélectionnez un produit à supprimer :", noms)
        if st.button("Supprimer"):
            sup_prd_streamlit(stock, nom_sel)
    else:
        st.info("📦 Le stock est vide.")

# ----- Modifier -----
elif choix == "Modifier la quantité d’un produit":
    if stock:
        noms = [p[0] for p in stock]
        nom_sel = st.selectbox("Produit à modifier :", noms)
        nouvelle_qte = st.number_input("Nouvelle quantité :", min_value=0, step=1)
        if st.button("Modifier"):
            mdf_qnt_streamlit(stock, nom_sel, nouvelle_qte)
    else:
        st.info("📦 Le stock est vide.")

# ----- Afficher -----
elif choix == "Afficher le stock":
    aff_stock_streamlit(stock)

# ----- Statistiques -----
elif choix == "Afficher les statistiques":
    stats_streamlit(stock)

# ----- Graphiques -----
elif choix == "Afficher un graphique":
    chart_type = st.radio("Choisir le type de graphique :", ["Bar chart", "Pie chart"])
    if chart_type == "Bar chart":
        visualize_bar_streamlit(stock)
    else:
        visualize_pie_streamlit(stock)
