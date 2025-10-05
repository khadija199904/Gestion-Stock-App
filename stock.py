stock = []

def ajt_prd():
    prd = input("Entrer votre produit sous frome (Produit,Quantite,Prix) : ")
    nom, qnt, prix_unit = prd.split(",")
    
    stock.append([nom.strip(), int(qnt), float(prix_unit)])
    print(f"{nom.strip()} ajouté au stock.")
    return stock

def sup_prd():
    nom = input("Entrer le nom de produit à supprimer : ")
    for p in stock:
        if p[0] == nom:
            stock.remove(p)
            print(f"{nom} supprimé.")
            return  
    print("Le produit n'existe pas !!!")

def mdf_qnt():
    nom = input("Nom de produit à modifier : ")
    for p in stock:
        if p[0] == nom:
            qnt = int(input("Nouvelle Quantité : "))
            p[1] = qnt
            print(f"Quantité de {nom} mise à jour.")
            return  
    print("Le produit n'existe pas !!!!")

def aff_stock():
    if not stock:
        print("Le stock est vide.")    
    else :
        print("Stock actuel :")
        for p in stock:
            print(f"- {p[0]} : quantité={p[1]}, prix={p[2]}")
            
