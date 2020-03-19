#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  Vol import *
from Client import *
import numpy 
hugeNumber = float("inf") 

#Definition des horaires des vols

class Time:

    def init(self,h,m):
        self.hours=h+m/60
        self.minutes=h*60+m

#Exemple d'instances pour l'horaire:
t1 = Time(8,30) #8h30
t1 = Time(12,30) #12h30



def utility(C,V):
    """fonction qui définit l'utilité du vol V pour le client C selon son jour d'arrivée
    fonction scalaire linéaire au prix et non linéaire en fonction de l'heure du vol"""
    return V.time_utility - C.alpha*V.proposal + C.erreur  #OK si on norme alpha et que on verifie que alpha reste positif. 



#!!!!!!!ALGO DE STOCHASTIC DP EN CHANTIER A RELIRE/AMELIORER/MODIFIER PAR JULIAN et FRANCOIS!!!!!!!!

#initialisation des paramètres pour les vols 
highest_numbered_state = 3*2 #taille du plus grand état = nombres de places dans les vols (3 par ex) x nombre de vols (2 par ex)
f = numpy.zeros([stages + 2, highest_numbered_state + 1]) #pour stocker la meilleur espérance de chaque state à chaque stage
x = numpy.zeros([stages + 1, highest_numbered_state + 1]) #pour stocker le pricing optimal nécessaire pour obtenir cette meilleur espérance 
vols_de_la_journée =  [v1,v2]  #liste de 2 vols par exemple
prices = [[30],[50],[100]] #les prix possibles pour chaque vol
states = [] #tous les états possibles pour un client : chaque vol à 30, 50 ou 100e ou plus de places dans ce vol 
for i in prices:
    states.append([i,[]])
    states.append([[],i])
    for j in prices:
        states.append([i,j])

#début de l'algorithme à proprement parler

for t in stages : #nouvelle étape, on est en backward (à parcourir à l'envers)
    for i in states :  #état =  liste du prix proposé au client (liste du prix pour chaque vol à cet étape)
        value = -hugeNumber  
        for d in pricing_options :  #decision du nouveau pricing pour chacun des 2 vols [30,30] [30,50] [50,50] ....
            esp = 0
            for r in (v1,v2,rien) : #le client choisi son vol en maximisant son utilité ou pas de vol
                j = état au stage t+1 
                esp += (probability of r)*((benef sur r) + f[t+1,j]) 

            if esp > value :  
                value = esp 
                bestMove = d 

        #on stock à l'étape t l'état i la fonction valeur bénéfice dans f et la décision de pricing dans x
        f[t,i] = value 
        x[t,i] = bestMove 

    # fin boucle states i
# fin boucle stages t 

print("la valeur optimale est " + str(f[1,(initial state)])) #on travaille en backward
print("A la première étape prendre la décision de pricing " + str(x[1, (initial state)]) 
for t in range(2,stages+1) : 
    print("A l'étape " + str(t) + ":") 
    for i in (possible states) : 
        print(" si on est dans l'état " + str(i) + ", prendre la décision de pricing " + str(x[t,i])
