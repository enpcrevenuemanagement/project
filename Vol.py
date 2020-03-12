import math

class Vol:

#Fonction chameau
time_preference = lambda x : (5 + math.cos(x-8) - (x-8)*math.cos(x-8))/12.3507
    
    #2 attributs : pricing et time_utility
    #pricing = Dico de chaque vol qui contient sa politique de prix pour les sièges restants. 
    #Chaque clé correspond à une classe de prix k, et à chaque classe de prix on associe le doublet 
    #(prix des places de cette classe, nombre de places restantes à vendre dans cette classe)
    #time_utility = fonction chameau pour l'utilité horaire commune à tous les clients et 
    #qui dépend uniquement de l'heure du vol

    def init(self,t,n):
        #Caractéristiques intrinsèques du vol: horaire et nombre de sieges total disponibles
        self.departure_time = t #en heures, en base 10
        self.seats = n #Type int

        self.pricing = {}

        self.time_utility = time_preference(t.hours)


        #Vecteur des prix des places déjà vendues
        self.sold = []

    #Methode pour créer un pricing pour un vol
    #arguments : k le nombres de classes sur ce vol, lp la liste des k prix par ordre croissant
    
    def new_pricing(self, k, lp):
        n = self.seats[0]//k #le nombre de places qu'on va pouvoir allouer à chaque classe
        for i in range(k): #ajout du nombre de place dans chaque classe au prix correspondant lp[k] 
            self.pricing[i] = [lp[i], n]
        self.pricing[0] = [lp[0], n+ self.seats%k] #et le reste va dans la catégorie 0

    #Méthode pour mettre à jour un pricing de vol, lorsque des places ont été vendues (à la fin de la journée): 
    #on récupère l'ancien dictionnaire et on en recrée un nouveau
    #on peut choisir pour ce nouveau pricing le nombre de classes k et les nouveaux prix à attribuer  

    def maj_pricing(self, k, lp):
        nb = 0 #nombre de places restantes sur le vol 
        for d in self.pricing:
            nb += d[1]
        n = nb//k
        for i in range(k): #ajout du nombre de place dans chaque classe au prix correspondant lp[k] 
            self.pricing[i] = [lp[i], n]
        self.pricing[0] = [lp[0], n+ nb%k] #et le reste va dans la catégorie 0

#Après chaque client on va décrementer le dictionnaire du  nombre de places restantes et on va augmenter 
# sold du nombre de places vendues, et à la fin de la journée on met à jour le pricing à partir de 
# l'ancien dico pour le redéfinir à partir des places restantes e fin de journée

    def proposal(self):
        return self.pricing[0][0]
