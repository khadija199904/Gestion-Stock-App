from stock import ajt_prd,aff_stock,mdf_qnt,sup_prd



while True :
    choix = input(" Voulez-vous ajouter un produit ? (o/n)")
    if choix == "o":
        ajt_prd()
        aff_stock()
    elif choix =="n":
        print("Fin !!!")
        break
    else :
        print("Réponse invalide !!!")

mdf_qnt()
sup_prd()
