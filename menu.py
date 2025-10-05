
from stock import ajt_prd, sup_prd, mdf_qnt,aff_stock, stock
from stats import stats
from visualize import visualize

def menu(stock):
    """Affiche le menu principal et gère les choix de l'utilisateur."""
    while True:
        print("\n=== MENU STOCK ===")
        print("1. Ajouter un produit")
        print("2. Afficher le stock")
        print("3. Statistiques")
        print("4. Visualiser (bar chart)")
        print("5. Quitter")

        choix = input("👉 Entrez votre choix : ")

        if choix == "1":
            while True:
                ajt_prd(stock)
                aff_stock(stock)
                continuer = input("Voulez-vous ajouter un autre produit ? (o/n) : ").lower()
                if continuer != "o":
                    break
        elif choix == "2":
            aff_stock(stock)
        elif choix == "3":
            stats(stock)
        elif choix == "4":
            visualize_bar(stock)
        elif choix == "5":
            print(" Fin du programme.")
            break
        else:
            print(" Choix invalide, réessayez.")