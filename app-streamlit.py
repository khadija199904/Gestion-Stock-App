import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# ========= STOCK GLOBAL =========
if "stock" not in st.session_state:
    st.session_state.stock = []

# ========= FONCTIONS STREAMLIT =========
def ajt_prd(stock, prd_input):
    try:
        nom, qnt, unit_prix = prd_input.split(",")
        stock.append([nom.strip(), int(qnt), float(unit_prix)])
        st.success(f"✅ {nom.strip()} ajouté au stock.")
    except ValueError:
        st.error("⚠️ Format invalide. Exemple : ProduitA,10,15.5")

def sup_prd(stock, nom):
    for p in stock:
        if p[0] == nom:
            stock.remove(p)
            st.warning(f"🗑️ {nom} supprimé du stock.")
            return
    st.error("❌ Produit introuvable.")

def mdf_qnt(stock, nom, nouvelle_qnt):
    for p in stock:
        if p[0] == nom:
            p[1] = nouvelle_qnt
            st.info(f"🔄 Quantité de {nom} mise à jour à {nouvelle_qte}.")
            return
    st.error("❌ Produit introuvable.")

def aff_stock(stock):
    st.subheader("📋 Tableau du stock actuel")
    if not stock:
        st.info("📦 Le stock est vide.")
    else:
        arr = np.array(stock, dtype=object)
        st.dataframe(
            {
                "Produit": arr[:, 0],
                "Quantité": arr[:, 1].astype(int),
                "Prix unitaire (DH)": arr[:, 2].astype(float),
                
            }
        )

def stats(stock):
    if not stock:
        st.info("📦 Le stock est vide.")
        return

    arr = np.array(stock, dtype=object)
    produits = arr[:, 0]
    qnt = arr[:, 1].astype(int)
    unit_prix = arr[:, 2].astype(float)

    valeur_totale = np.sum(qnt * unit_prix)
    prix_moyen = np.mean(unit_prix)
    min_prix = np.min(unit_prix)
    max_prix = np.max(unit_prix)

    produit_plus_cher = produits[np.argmax(unit_prix)]
    produit_moins_cher = produits[np.argmin(unit_prix)]

    st.subheader("📊 Statistiques du stock")
    st.write(f"Valeur totale du stock : **{valeur_totale:.2f} DH**")
    st.write(f"Prix moyen unitaire : **{prix_moyen:.2f} DH**")
    st.write(f"Prix minimum : {min_prix}")
    st.write(f"Prix Maximum : {max_prix}")
    st.write(f"Produit le plus cher : {produit_plus_cher}")
    st.write(f"Produit le moins cher : {produit_moins_cher}")

def visualize_bar(stock):
    if not stock:
        st.info("📦 Le stock est vide.")
        return

    arr = np.array(stock, dtype=object)
    produits = arr[:, 0]
    valeurs = arr[:, 1].astype(float) * arr[:, 2].astype(float)

    fig, ax = plt.subplots()
    ax.bar(produits, valeurs, color="skyblue")
    ax.set_xlabel("Produits")
    ax.set_ylabel("Valeur totale (DH)")
    ax.set_title("Valeur du stock par produit")
    st.pyplot(fig)

def visualize_pie(stock):
    if not stock:
        st.info("📦 Le stock est vide.")
        return

    arr = np.array(stock, dtype=object)
    produits = arr[:, 0]
    valeurs = arr[:, 1].astype(float) * arr[:, 2].astype(float)

    fig, ax = plt.subplots()
    ax.pie(valeurs, labels=produits, autopct="%1.1f%%", startangle=90)
    ax.set_title("Répartition de la valeur du stock")
    st.pyplot(fig)

# ========= INTERFACE =========
st.title("📦 Application de Gestion du Stock")

menu = [
    "Ajouter un produit",
    "Supprimer un produit",
    "Modifier une quantité",
    "Afficher le stock",
    "Statistiques",
    "Visualiser le stock"
]

choix = st.sidebar.selectbox("Menu", menu)
stock = st.session_state.stock

# ----- Ajouter -----
if choix == "Ajouter un produit":
    prd_input = st.text_input("Entrer le produit (Nom,Quantité,Prix)")
    if st.button("Ajouter"):
        ajt_prd(stock, prd_input)
    aff_stock(stock)

# ----- Supprimer -----
elif choix == "Supprimer un produit":
    if stock:
        noms = [p[0] for p in stock]
        nom_sel = st.selectbox("Produit à supprimer :", noms)
        if st.button("Supprimer"):
            sup_prd(stock, nom_sel)
        aff_stock(stock)
    else:
        st.info("📦 Le stock est vide.")

# ----- Modifier -----
elif choix == "Modifier une quantité":
    if stock:
        noms = [p[0] for p in stock]
        nom_sel = st.selectbox("Produit à modifier :", noms)
        nouvelle_qte = st.number_input("Nouvelle quantité :", min_value=0, step=1)
        if st.button("Modifier"):
            mdf_qnt(stock, nom_sel, nouvelle_qte)
        aff_stock(stock)
    else:
        st.info("📦 Le stock est vide.")

# ----- Afficher -----
elif choix == "Afficher le stock":
    aff_stock(stock)

# ----- Statistiques -----
elif choix == "Statistiques":
    stats(stock)

# ----- Visualiser -----
elif choix == "Visualiser le stock":
    chart_type = st.radio("Choisir le type de graphique :", ["Bar chart", "Pie chart"])
    if chart_type == "Bar chart":
        visualize_bar(stock)
    else:
        visualize_pie(stock)
