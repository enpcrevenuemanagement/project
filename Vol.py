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
        #Nombre de sièges restants
        self.remaining = n
 

    #Méthode pour mettre à jour vol lorsqu'une place est vendue
    def sell(self):
        if self.remaining > 0:
            self.sold.append(self.price)
            self.remaining -= 1
            
    def profit(self):
        return sum(self.sold)

