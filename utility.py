### MODELES DE PREFERENCES
import numpy as np
import math

#Fonction utilité du client relative à l'horaire h du vol (chameau)
#Fonction entre 0 et 1 ?
def time_utility(C,V):
    res = lambda h : (5 + math.cos(h-8) - (h-8)*math.cos(h-8))/12.3507
    return res(V.time_departure)

#Fonction avec les 2 paliers comme axel nous a montré
#varie entre 0 et 1.
def time_decay_utility(C):
    res = lambda h : (12 + math.sin(h)-h)/12
    return res(C.time_range)

#Fonction utilité du client relative au prix p, selon le temps t (jour d'arrivée)
#varie entre 1 et 0
def price_utility(C,V):
    return math.exp(-time_decay_utility(C)*V.price)

#Partie déterministe vi(xj) de l'utilité du vol V pour le client C
def utility(C,V):
    theta = 1
    return theta * price_utility(C,V) + time_utility(C,V)

#Selon une liste de vols Vi flights de longueur n, choix du client C selon loi logit multinomiale
#On définit la variable de choix yi par la PMF
#v0 est l'utilité du choix 0
def choice(C,flights,v0):
    n = len(flights)
    choices = [k for k in range(n+1)]
    utilities = [math.exp(v0)]
    for flight in flights:
        utilities.append(math.exp(utility(C,flight)))
    s = sum(utilities)
    probabilities = [u/s for u in utilities]
    return np.random.choice(choices, 1, p=probabilities)

#proba que le client C choisisse le vol V parmi une liste flights
#v0 est l'utilité du choix 0
def proba_c_v(C,V,flights,v0): 
    utilities = [math.exp(v0)]
    for flight in flights:
        utilities.append(math.exp(utility(C,flight)))
    s = sum(utilities)
    probability = math.exp(utility(C,V))/s
    return probability

#probabilité de ne chosisir aucun vol
def proba_v0(C,flights, v0): 
    utilities = [math.exp(v0)]
    for flight in flights:
        utilities.append(math.exp(utility(C,flight)))
    s = sum(utilities)
    probability = math.exp(v0)/s
    return probability

