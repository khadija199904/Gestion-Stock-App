import matplotlib.pyplot as plt 
import numpy as np
def visualize(stock) :
     if not stock:
        print("⚠️ Le stock est vide.")
        return
     product = np.array([item[0] for item in stock])
     Qnt = np.array([item[1] for item in stock])
     Unit_Price = np.array([item[2] for item in stock])
     
     # Valeur par produit
     valeurs = prix * quantite
     
     plt.figure(figsize=(10, 6))
     plt.bar(product,Qnt,color='skyblue')
     plt.xlabel('Quantité')
     plt.ylabel('Produit')
     plt.title('Quantité par produit')
     plt.show()

     # Tracé du camembert
     plt.figure(figsize=(6, 6))
     plt.pie(valeurs, labels=product, autopct="%1.1f%%", startangle=140)
     plt.title("Répartition de la valeur totale du stock par produit")
     plt.show()



