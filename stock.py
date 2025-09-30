stock = []

def ajt_prd():
    prd = input("Entrer votre produit sous forme (Produit,Quantite,Prix) : ")
    nom, qnt, prix_unit = prd.split(",")
    qnt = int(qnt)
    prix_unit = float(prix_unit)
    stock.append([nom, qnt, prix_unit])
    print(f"{nom} ajouté au stock.")
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
    nom = input("Nom du Produit à modifier : ")
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
        return
    print("Stock actuel :")
    for p in stock:
        print(f"- {p[0]} : quantité={p[1]}, prix={p[2]}")
