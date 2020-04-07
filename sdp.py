from  Vol import *
from Client import *
from demand import *
from utility import *
from time import *
import numpy 
import itertools
hugeNumber = float("inf")


def States(flights):
    n = len(flights)
    arg = [range(f.seats+1) for f in flights]
    states = []
    for state in itertools.product(*arg):  
            states.append({flights[i]: state[i] for i in range(n)})
    return states

def Pricing_options(prices, flights):
    n = len(flights)
    arg = [prices for i in range (n)]
    pricing_options = []
    for pricing_option in itertools.product(*arg):
        if pricing_option not in pricing_options :
            pricing_options.append(pricing_option)
    return pricing_options


def SDP(prices, flights, N): #prix possibles, vols, et nombre de clients 
    #définition des états possibles {v1:places vendues, v2:places vendues, ...}
    states = States(flights)
    #définition du pricing :  [p1,p2,...]
    pricing_options = Pricing_options(prices, flights)
    #matrice de l'espérance futur des gains
    f = [[0 for k in range(len(states))] for l in range(N+1)]  
    #matrice des décisions 
    x = [[[] for k in range(len(states))] for l in range(N+1)]  

    for t in reversed(range(N)) : #nouvelle étape, on est en backward (à parcourir à l'envers)
        for state in states:  #états accessibles à l'étape t, toutes les paires possibles de vecteur sold
            value = -hugeNumber 
            bestMove = [] 

            for d in pricing_options :  #decision du nouveau pricing pour chacun des vols  
                esp = 0

                #on va d'abord voir si dans cet état des vols sont déja pleins: 
                for f in flights:
                    if  state[f] == f.seats: #si c'est le cas, on ne proposera pas de place au client pour ce vol
                        i = flights.index(f)
                        d[i] = hugeNumber     #on propose un prix infini

                #on affecte maintenant chaque prix au vol correspondant 
                for j in range(len(flights)):
                    flights[j].price = d[j]  

                #les prix sont à jour, on calcule l'espérance de gains futurs de t à N.
                for f in flights : #le client choisi son vol en maximisant son utilité ou pas de vol 
                    new_state = state
                    new_state[f] += 1 #nouvel état qui correspond à une place de plus vendue sur ce vol
                    esp += (proba que le client n choisisse f)*f.price + f[t+1][states.index(new_state)] 

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
 
