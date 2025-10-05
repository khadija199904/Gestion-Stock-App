import numpy as np
from stock import  stock

def stats() :
    global stock
    if not stock:  # Vérifier si le stock est vide
        print("⚠️ Le stock est vide.")
        return
    product = np.array([item[0] for item in stock])
    Qnt = np.array([item[1] for item in stock])
    Unit_Price = np.array([item[2] for item in stock])
    
    # Valeur totale du stock (somme(prix * quantité))
    Total_stock = sum(Qnt*Unit_Price)
    # Prix moyen des produits
    AVR_price = np.mean(Unit_Price)
    
    #Prix minimum et maximum
    Min_Price = np.min(Unit_Price)
    Max_Price = np.max(Unit_Price)
     
    
    # Produits le plus cher
    produit_plus_cher = product[np.argmax(Unit_Price)]
    
    # Produits le moins cher
    produit_moins_cher = product[np.argmin(Unit_Price)]
    


    print("Statistiques du stock :")
    print(f"Valeur totale du stock : {Total_stock}")
    print(f"Prix moyen des produits : {AVR_price:.2f}")
    print(f"Prix minimum : {Min_Price}")
    print(f"Prix Maximum : {Max_Price}")
    print(f"Produit le plus cher : {produit_plus_cher}")
    print(f"Produit le moins cher : {produit_moins_cher}")
    
