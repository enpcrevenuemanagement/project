### MODELES DE PREFERENCES

import numpy as np
import math

#Modèle de sensibilité au prix selon le temps t (jour)
#Modèle linéaire décroissant variant entre t0=0 et tf
#tf est le nombre de jours d'ouverture de la billetterie, 30 jours par ex
def alpha(t):
    alpha_0=10
    alpha_f=1
    tf=30
    return alpha_0 + t/tf * (alpha_f - alpha_0)

#Fonction utilité du client relative au prix p, selon le temps t (jour d'arrivée)
def price_utility(C,V):
    return math.exp(-alpha(C.time_range)*V.price)

#Fonction utilité du client relative à l'horaire h du vol (chameau)
#Fonction entre 0 et 1 ?
def time_utility(C,V):
    res = lambda h : (5 + math.cos(h-8) - (h-8)*math.cos(h-8))/12.3507
    return res(V.time_departure)

#Partie déterministe vi(xj) de l'utilité du vol V pour le client C
def utility(C,V):
    theta = 1
    return theta * price_utility(C,V) + time_utility(C,V)

#Selon une liste de vols Vi flights de longueur n, choix du client Cd'un vol ou de 0
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

