### MODELES DE PREFERENCES
import numpy as np
import math

from vol import *
from client import *

#Fonction utilité du client relative à l'horaire h du vol (chameau)
# [0,1] ==> [0,1] 

def time_utility(C,V):
    # Prend en entrée l'horaire normalisé dans la journée (cf classe Horaire) entre 0 et 24
    # Pics d'utilité 1 à 9 et 19h
    # Utilité 0.25 à 5h, 14h et 23h

    res = lambda h : math.exp(-1/12*(h-9)**2) + math.exp(-1/12*(h-19)**2)
    return res(V.departure_time.hours)

#Fonction utilité du client relative au prix p, selon le temps t (jour d'arrivée)
# R ==> [0,1]

def price_utility(C,V):

    price_scale = 100

    #utilité négative
    return 1 - V.price / price_scale

#Partie déterministe vi(xj) de l'utilité du vol V pour le client C 
# ==> [0,1/temp] 
def utility(C,V):
    return (C.theta() * time_utility(C,V) + ( 1 - C.theta() ) * price_utility(C,V))

#Selon une liste de vols Vi flights de longueur n, choix du client C selon loi logit multinomiale
#On définit la variable de choix yi par la PMF
#v0 est l'utilité du choix -1

def choice(C,flights):
    n = len(flights)
    #0 à n-1 pour les n vols et -1 si pas d'achat
    choices = [-1]
    u = [C.v0/C.temp]

    for i in range(n):
        flight = flights[i]
        if flight.remaining > 0:
            u.append( utility(C,flight) / C.temp )
            choices.append(i)

    probas = np.exp(u)/sum(np.exp(u))
    #print(">>>Le client peut acheter l'un des vols pour les valeurs d'utilité: {} et de probabilité: {}".format(utilities[1:],probabilities[1:]))
    return np.random.choice(choices, 1, p=probas)[0]
