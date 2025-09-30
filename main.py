<<<<<<< HEAD

from stock import ajt_prd, sup_prd, mdf_qnt,aff_stock, stock
from stats import stats


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


sup_prd()
mdf_qnt()
stats(stock)
=======
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
>>>>>>> 6884e05e83bd91543a1d0c6915af1f6180a1cb4a
