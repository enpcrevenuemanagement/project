from vol import *
from client import *
from utility import *
from time import *
import numpy 
import itertools


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
            pricing_options.append(list(pricing_option))
    return pricing_options

#proba que le client C choisisse le vol V parmi une liste flights: SEULEMNT SIL  RESTE DES PLACES
#v0 est l'utilité du choix 0
def proba_c_v(C,V,flights,vols_pleins): 
    n = len(flights)
    #0 à n-1 pour les n vols et -1 si pas d'achat
    choices = [-1]
    u = [C.v0 / C.temp]

    for i in range(n):
        flight = flights[i]
        if flight.remaining > 0:
            u.append( utility(C,flight) / C.temp )
            choices.append(i)

    proba = np.exp( utility(C,V) / C.temp ) / sum(np.exp(u))
    return proba

#probabilité de ne chosisir aucun vol
def proba_v0(C,flights,vols_pleins): 
    n = len(flights)
    #0 à n-1 pour les n vols et -1 si pas d'achat
    choices = [-1]
    u = [C.v0 / C.temp]

    for i in range(n):
        flight = flights[i]
        if flight.remaining > 0:
            u.append( utility(C,flight) / C.temp )
            choices.append(i)

    proba = np.exp( C.v0 / C.temp ) / sum(np.exp(u))
    return proba

def SDP(prices, flights, N): #prix possibles, vols, nombre de clients
    #définition des états possibles {v1:places vendues, v2:places vendues, ...}
    states = States(flights)
    #définition du pricing :  [p1,p2,...]
    pricing_options = Pricing_options(prices, flights)
    #matrice de l'espérance futur des gains
    F = [[0 for k in range(len(states))] for l in range(N+1)]  
    #matrice des décisions 
    x = [[["N/A" for j in range(len(flights))] for k in range(len(states))] for l in range(N)]  
    
    for t in reversed(range(N)) : #nouvelle étape, on est en backward (à parcourir à l'envers)
        #création d'un client type pour cette étape (uniquement pour calculer la probabilité avec C.time_range = t)
        ti=t/N
        C = Client(ti)
        for state in states:  #états accessibles à l'étape t, toutes les paires possibles de vecteur sold

            #Dans l'état state, on regarde si des vols sont pleins
            #on va d'abord voir si dans cet état des vols sont déja pleins: 
            vols_pleins = []

            for f in flights:
                if  state[f] == f.seats: #si c'est le cas, on ne proposera pas de place au client pour ce vol
                    vols_pleins.append(f)    #on stock ce vol 

            for d in pricing_options :  #decision du nouveau pricing pour chacun des vols  
                esp = 0

                #on affecte maintenant chaque prix au vol correspondant 
                for j in range(len(flights)):
                    flights[j].price = d[j]  

                for f in flights : #le client choisi son vol en maximisant son utilité ou pas de vol 
                    if f not in vols_pleins:
                        new_state = state.copy()
                        new_state[f] += 1 #nouvel état qui correspond à une place de plus vendue sur ce vol
                        esp += proba_c_v(C,f,flights,vols_pleins)*(f.price + F[t+1][states.index(new_state)])

                #cas où le client t ne choisit aucun vol
                #p0(t) la proba associée, on reste dans le même état à t+1 et pas de bénéfices engendrés à t
                esp += proba_v0(C,flights,vols_pleins)*F[t+1][states.index(state)]
                
    #nécessité de passer en backward : des qu'on calcule le nouvel état qui correspond à l'issue de la vente on doit savoir quel est le resultat de l'espérance
    #des gains de ce nouvel état de t+1 à n pour calculer l'espérance de gains globale de t à n.
                
                if esp > F[t][states.index(state)]:
                    F[t][states.index(state)] = esp
                    x[t][states.index(state)] = d.copy()   #si l'esperance de gain est maximale pour une decision de pricing, on stock la valeur et la decision associée
        # fin boucle states i

        ### DETECTER DES VOLS PLEINS ET ADAPTER LE PRICING POUR L'INDIQUER
            for f in flights:
                if f in vols_pleins:
                    x[t][states.index(state)][flights.index(f)] = "Full"

    # fin boucle stages t

    return F,x

