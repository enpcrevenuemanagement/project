import math

#Definition d'un format pour représenter l'horaire
class Horaire:

    def __init__(self,h,m):
        #Nombre d'heures au format décimal entre minuit et l'horaire considéré
        self.hours=h+m/60
        #Nombre de minutes entre minuit et l'horaire considéré
        self.minutes=h*60+m
        #Valeur normalisée entre 0 et 1
        self.norm = self.hours/24

    def __str__(self):
        return str(self.minutes//60)+":"+str(self.minutes%60)

#Modélisation des caractéristiques propres à chaque vol 

class Vol:

    def __init__(self,departure_time,seats):
        #Caractéristiques immuables du vol
        self.departure_time = departure_time #instance de la classe Horaire
        self.seats = seats #Type int

        #Variables

        #Prix affiché pour le client
        self.price = 0
        #Prix des sièges vendus
        self.sold = []
        #Nombre de sièges restants
        self.remaining = seats
 

    #Méthode pour mettre à jour vol lorsqu'une place est vendue
    def sell(self):
        if self.remaining > 0:
            self.sold.append(self.price)
            self.remaining -= 1
            
    def gain(self):
        return sum(self.sold)

    def reset(self):
        #Prix affiché pour le client
        self.price = 0
        #Prix des sièges vendus
        self.sold = []
        #Nombre de sièges restants
        self.remaining = self.seats


