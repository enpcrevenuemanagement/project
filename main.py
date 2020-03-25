#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  Vol import *
from Client import *
import numpy 
hugeNumber = float("inf")
N = 4 #nombre d'intervalles de temps

#Definition d'un format pour représenter l'horaire
class Time:

    def __init__(self,h,m):
        #Nombre d'heures au format décimal entre minuit et l'horaire considéré
        self.hours=h+m/60
        #Nombre de minutes entre minuit et l'horaire considéré
        self.minutes=h*60+m

    def __str__(self):
        return str(self.minutes//60)+":"+str(self.minutes%60)

def demand_simulator(N):
    """ fonction qui renvoie list_of_clients, une liste de clients à partir de N, le nombre d'intervalle de temps"""
    list_of_clients=[]
    for k in range(N):
        if numpy.random.randint(0,1) > 0 : #condition pour savoir s'il y a un client à l'intervalle de temps k 
            C= Client(k)
            L.append(C)
    return list_of_clients


# MODELES DE PREFERENCES

def utility(C,V):
    """fonction qui définit l'utilité du vol V pour le client C selon son jour d'arrivée
    fonction scalaire linéaire au prix et non linéaire en fonction de l'heure du vol"""
    return V.time_utility - C.alpha*V.proposal + C.erreur  #OK si on norme alpha et que on verifie que alpha reste positif. 



#!!!!!!!ALGO DE STOCHASTIC DP EN CHANTIER A RELIRE/AMELIORER/MODIFIER PAR JULIAN et FRANCOIS!!!!!!!!

#initialisation des paramètres pour les vols 
vols_de_la_journée =  [v1,v2]  #liste de 2 vols de 2 places chacuns 
#définition des états : chaque état est la liste des vecteurs v.sold possibles
prices = [30,50,100] #les prix possibles pour chaque vol
#constructeur bourrin des états possibles avec le vecteur prices et 2 vols de 2 places chacuns(j'ai pas trouvé plus simple...)
states = []
for i in prices:
    for j in prices:
        states.append([[i],[j]])
        states.append([[i],[]])
        states.append([[],[j]])
        states.append([[],[i,j]])
        states.append([[i,j],[]])
        states.append([[],[]])
        for k in prices:
            states.append([[i,j],[k]])
            states.append([[i],[j,k]])
            for l in prices:
                states.append([[i,j],[k,l]])
for k in states: #on retire les doublons
        c=states.count(k)
        if c>1:
            states.remove(k)
#Pour 2 vols de 2 places chacuns et 2 prix possibles : 50 états possibles 
#Pour 2 vols de 2 places chacuns et 3 prix possibles : 173 états possibles! 
#Pour 2 vols de 2 places chacuns et 4 prix possibles : 450 états possibles! 

#définition du pricing : chaque pricing est un vecteur de prix (1 prix par vol)
pricing_options = []
for i in prices:
    for j in prices:
        if [i,j] not in pricing_options:
            pricing_options.append([i,j])
print(pricing_options)

f = numpy.zeros([N+1, len(states)]) #pour stocker la meilleur espérance de chaque state à chaque stage
x = numpy.zeros([N=1, len(states)]) #pour stocker le pricing optimal nécessaire pour obtenir cette meilleur espérance 
dic = {} #pour stocker le pricing optimal
count = 0
for t in reversed(range(N)) : #nouvelle étape, on est en backward (à parcourir à l'envers)
    for i in states:  #états accessibles à l'étape t  i = [v1.sold, v2.sold]
        value = -hugeNumber  
        for d in pricing_options :  #decision du nouveau pricing pour chacun des 2 vols [30,30] [30,50] [50,50] ....
            esp = 0
            for r in range(2) : #le client choisi son vol en maximisant son utilité ou pas de vol, 0 = pas de vol, 1=v1 et 2=v2
                if r == 0: #s'il ne choisi pas de vol on reste dans le même état
                    state = i 
                    esp += (probability of r = 0)*0 + f[t+1,states.index(state)] #le bénéfice associé à ce cas de figure est nul
                else : #il choisit le vol 1 ou 2
                    state = i
                    state.append(d[r-1]) #on passe dans un nouvel état : celui qui correspond à la vente d'une place de plus au prix d[r-1] sur le vol r
                    esp += (probability of r)*d[r-1] + f[t+1,states.index(state)] #le bénéfice associé à ce cas de figure est d[r-1]
#nécessité de passer en backward : des qu'on calcule le nouvel état qui correspond à l'issue de la vente on doit savoir quel est le resultat de l'espérance 
#des gains de ce nouvel état de t+1 à n pour calculer l'espérance de gains globale de t à n.
            if esp > value :  
                value = esp 
                bestMove = d
                dic[count] = bestMove


        #on stock à l'étape t l'état i la fonction valeur bénéfice dans f et la décision de pricing dans x
        f[t,states.index(i)] = value 
        x[t,states.index(i)] = count
        count += 1

    # fin boucle states i
# fin boucle stages t 


print("la valeur optimale est " + str(f[1,[[],[]]]))
print("A la première étape prendre la décision de pricing " + str(x[1,[[],[]]]) )
for t in range(2,N):
    print("A l'étape " + str(t) + ":") 
    for i in states: 
        print(" si on est dans l'état " + ' '.join(str(elem) for elem in i[0]) + " -- " + ' '.join(str(elem) for elem in i[1]) + ", prendre la décision de pricing " + str(dic[x[t,states.index(i)]]))

 
