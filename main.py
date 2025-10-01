from stock import ajt_prd, sup_prd, mdf_qnt,aff_stock, stock
from stats import stats
from visualize import visualize


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
visualize(stock)