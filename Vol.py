import math


#Modélisation des caractéristiques propres à chaque vol 
#Cela exclut tout ce qui dépend aussi du client (utilité du client pour le vol entre autres ==> utility.py)

class Vol:

    def init(self,t,n):
        #Paramètres immuables du vol
        self.departure_time = t #en heures, en base 10
        self.seats = n #Type int
        #Variables
        #Prix affiché pour le client
        self.price = 0
        #Prix des sièges vendus
        self.sold = []
 
    #Méthode pour mettre à jour le prix du vol, lorsque une place a été vendue après un client  
    #on l'ajoute dans sold au prix ou elle a été vendue
    #on met à jour le nouveau prix de vente x

    def maj_pricing(self, x):
        self.sold.append(self.price)
        self.price = x

    def profit(self):
        return sum(self.sold)

