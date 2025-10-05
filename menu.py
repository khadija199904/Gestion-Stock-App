
from stock import ajt_prd, sup_prd, mdf_qnt,aff_stock, stock
from stats import stats
from visualize import visualize_bar,visualize_pie

def menu(stock):
    """Affiche le menu principal et gère les choix de l'utilisateur."""
    while True:
        print("\n=== MENU STOCK ===")
        print("1. Ajouter un produit")
        print("2. Supprimer un produit")
        print("3. Modifier la quantité d’un produit")
        print("4. Afficher le stock")
        print("5. Afficher les statistiques")
        print("6. Afficher un graphique (bar chart ou pie chart)")
        print("7. Quitter")

        choix = input("👉 Entrez votre choix : ")

        if choix == "1":
            while True:
                ajt_prd()
                aff_stock()
                continuer = input("Voulez-vous ajouter un autre produit ? (o/n) : ").lower()
                if continuer != "o":
                    break
        elif choix == "2":
            sup_prd()
        elif choix == "3":
            mdf_qnt()
        elif choix == "4":
            aff_stock()
        elif choix == "5":
            stats(stock)
        elif choix == "6":
            print("\n=== Type de graphique ===")
            print("a. Bar chart")
            print("b. Pie chart")
            sous_choix = input("👉 Entrez votre choix (a/b) : ").lower()
            if sous_choix == "a":
                visualize_bar(stock)
            elif sous_choix == "b":
                visualize_pie(stock)
            else:
                print(" Choix invalide pour le graphique.")
        elif choix == "7":
            print(" Fin du programme.")
            break
        else:
            print(" Choix invalide, réessayez.")