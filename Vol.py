import math
from horaire import *


#Modélisation des caractéristiques propres à chaque vol 
#Cela exclut tout ce qui dépend aussi du client (utilité du client pour le vol entre autres ==> utility.py)

class Vol:

    def __init__(self,t,n):
        #Paramètres immuables du vol
        h,m = t
        self.departure_time = Horaire(h,m) #instance de la classe Horaire
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
            
    def gain(self):
        return sum(self.sold)

