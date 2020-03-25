#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  Vol import *
from Client import *
import numpy 
hugeNumber = float("inf")
N = 5 #nombre d'intervalles de temps

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
    #Partie déterministe Ui(xj) de l'utilité du vol V pour le client C
    return theta* + V.time_utility + C.erreur #le terme p(i,j) manque







# ALGORITHME DE SDP

#Initialize all needed parameters and data 
stages = 3 #nombre de stages
highest_numbered_state =  #taille du plus grand état = nombres de places dans les vols x nombre de vols
f = numpy.zeros([stages + 2, highest_numbered_state + 1]) 
x = numpy.zeros([stages + 1, highest_numbered_state + 1]) 


#If not zero, set each f[stages+1,i] to the terminal value of being in state i at the end For forbidden terminal states, use hugenumber for minimization, -hugenumber for maximization 
vols_de_la_journée = liste de 1 à 4 vols 
states = [vol_k.sold] for vol_k in vols_de_la_journée 

for t in range(stages,0,-1) : 
    for i in (states) : 
    #Determine set of decisions d which are possible in this stage/state combination value = -hugeNumber if maximizing or hugenumber if minimizing 
        for d in (set of allowed decisions d) : 
        #Compute rewards/costs that are not random 
        moveValue = (net rewards/costs that are not random) 

            for r in (set of random outcomes r) : 
                j = (resulting next state) #Compute rewards/costs that depend on r 
                moveValue += (probability of r)*((rewards/costs depending on r) + f[t+1,j]) 
                # If net present value is involved, beta*f[t+1,j]) instead, where 
                # beta = 1/(1 + r) is the discount factor 

            if moveValue > value : (use < instead of > if minimizing) 
                value = moveValue 
                bestMove = d 

        # End of d loop 
        f[t,i] = value 
        x[t,i] = bestMove 

    # End of i loop 
# End of t loop 

print("Optimal solution value is " + str(f[1,(initial state)])) 
print("In stage 1, (describe decision) " + str(x[1, (initial state)]) 
for t in range(2,stages+1) : 
    print("In stage " + str(t) + ":") 
    for i in (possible states) : 
        print(" If (describe state) " + str(i) + ", (describe decision) " + str(x[t,i])

