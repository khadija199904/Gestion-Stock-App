def stats (Stock) :
    Total_stock = sum(sctock[qnt]*stock[prix_Unit])
    print(f"Valeur totale du stock : {Total_stock }")

    AVR_price = np.mean(Stock[prix_Unit])
    print(f"Prix moyen des produits : {AVR_price}")

    Min_Price = np.min(sctock[prix_Unit])
    Max_Price = np.max(sctock[prix_Unit])
    print(f"Prix minimum : {Min_Price}")
    print(f"Prix Maximum : {Max_Price}")
    
    Unit_Price = np.array([item[2] for item in stock])
    # l'indice du prix maximum
    indice_max = np.argmax(Unit_Price)
    produit_cher = stock[indice_max]
    print(f"Produit le plus cher : {produit_cher}")
     
    indice_min = np.argmin(Unit_Price)
    produit_cher = stock[indice_max]
    print(f"Produit le plus cher : {produit_cher}")


