from  Vol import *
from Client import *
from demand import *
from utility import *
from time import *
import numpy 
hugeNumber = float("inf")



def States(flights):  #états possibles pour flights 
    n = len(flights)
    states = []
    if n == 2:
        for i in range(flights[0].seats+1):
            for j in range(flights[0].seats+1):
                states.append({flights[0]:i, flights[1]:j})
    if n == 3:
        for i in range(flights[0].seats+1):
            for j in range(flights[0].seats+1):
                for k in range(flights[0].seats+1):
                    states.append({flights[0]:i, flights[1]:j, flights[2]:k})
    if n == 4:
        for i in range(flights[0].seats+1):
            for j in range(flights[0].seats+1):
                for k in range(flights[0].seats+1):
                    for l in range(flights[0].seats+1):
                        states.append({flights[0]:i, flights[1]:j, flights[2]:k, flights[3]:l})
    return states


def Pricing_options(prices, flights):
    n = len(flights)
    pricing_options = []
    if n == 2:
        for i in prices:
            for j in prices:  
                if [i,j] not in pricing_options:
                    pricing_options.append([i,j])
    if n == 3:
        for i in prices:
            for j in prices:  
                for k in prices:
                    if [i,j,k] not in pricing_options:
                        pricing_options.append([i,j,k])
    if n == 4:
        for i in prices:
            for j in prices:  
                for k in prices:
                    for l in prices:
                    if [i,j,k,l] not in pricing_options:
                        pricing_options.append([i,j,k,l])
    return pricng_options


def SDP(prices, flights, N): #prix possibles, vols, et nombre de clients 
    #définition des états possibles {v1:places vendues, v2:places vendues, ...}
    states = States(flights)
    #définition du pricing :  [p1,p2,...]
    pricing_options = Pricing_options(prices, flights)
    #matrice f où on stock le gain futur maximal (espérance) f[i][j] si on est dans l'état j au pas de temps i
    f = [[0 for k in range(len(states))] for l in range(N+1)]  
    #matrice x de la même taille où on stock la décision de pricing optimale associée à ce gain f[i][j]
    #autrement dit il faut prendre la décision x[i][j] si on est dans l'état j à i, et alors le gain maximal 
    #qu'on pourra espérer avoir à la fin est f[i][j]
    x = [[[0,0] for k in range(len(states))] for l in range(N+1)]  

    for t in reversed(range(N)) : #nouvelle étape, on est en backward (à parcourir à l'envers)
        for i in states:  #états accessibles à l'étape t, toutes les paires possibles de vecteur sold
            value = -hugeNumber 
            bestMove = [] 
            for d in pricing_options :  #decision du nouveau pricing pour chacun des 2 vols [30,30] [30,50] [50,50] ....
                for i in range(len(flights)):
                    flights[i].price = d[i]  #affectation du prix à chaque vol
                esp = 0
                for f in flights : #le client choisi son vol en maximisant son utilité ou pas de vol 
                    state = i 
                    state[f] += 1 #nouvel état qui correspond à une place de plus vendue
                    esp += (proba que le client n choisisse f)*f.price + f[t+1][states.index(state)] #le bénéfice associé à ce cas de figure est d[r-1]
    #nécessité de passer en backward : des qu'on calcule le nouvel état qui correspond à l'issue de la vente on doit savoir quel est le resultat de l'espérance
    #des gains de ce nouvel état de t+1 à n pour calculer l'espérance de gains globale de t à n.
                if esp > value :  
                    value = esp
                    bestMove = d   #si l'esperance de gain est maximale pour une decision de pricing, on stock la valeur et la decision associée

            #on stock à l'étape t et à l'état i la fonction valeur bénéfice dans f et la décision de pricing dans x
            f[t][states.index(i)] = value
            x[t][states.index(i)] = bestMove

        # fin boucle states i
    # fin boucle stages t
    return f,x
 
