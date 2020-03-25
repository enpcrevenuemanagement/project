import math

time_preference = lambda x : (5 + math.cos(x-8) - (x-8)*math.cos(x-8))/12.3507

class Vol:

    
    #time_utility = fonction chameau pour l'utilité horaire commune à tous les clients et 
    #qui dépend uniquement de l'heure du vol

    def init(self,t,n):
        self.departure_time = t #en heures, en base 10
        self.seats = n #Type int
        self.pricing = []
        self.time_utility = time_preference(t.hours)
        self.sold = []
 
    #Au début on initialise toutes les places avec le même prix p (pas d'interet de les segmenter vu qu'on met à jour à chaque fois)
    
    def new_pricing(self, p):
        for i in range(self.seats):  
            self.pricing[i] = p
 
    #Méthode pour mettre à jour un pricing de vol, lorsque une place a été vendue après un client  
    #on supprime la place vendue de la liste, on l'ajoute dans sold au prix ou elle a été vendue
    #on met à jour au nouveau prix de vente x le pricing avec une place de moins dans l'avion

    def maj_pricing(self, x):
        self.sold.append(self.pricing.pop([0]))
        for k in range(len(self.pricing)):
            self.pricing[k] = x

    def proposal(self):
        if len(self.pricing) > 0:
            return self.pricing[0]
            
    def profit(self):
        return sum(self.sold)

