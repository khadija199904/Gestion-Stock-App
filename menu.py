
from stock import ajt_prd, aff_stock
from stats import stats
from visualize import visualize_bar

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
            ajt_prd(stock)
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