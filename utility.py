### MODELES DE PREFERENCES
import numpy as np
import math

from vol import *
from horaire import *
from client import *

#Fonction utilité du client relative à l'horaire h du vol (chameau)
# [0,1] ==> [0,1] 

def time_utility(C,V):
    #Prend en entrée l'horaire normalisé dans la journée (cf classe Horaire) entre 0 et 1 
    res = lambda h : 1/3.125 * ( 2 + math.cos(2*math.pi*(h-0.5)) + math.cos(2*math.pi*(h-0.25)/0.5) )
    return res(V.departure_time.norm)

#Sensibilité au prix avec les 2 paliers comme axel nous a montré
# [0,1] ==> [0,1]

def time_decay_utility(C):
    #Prend en entrée time_range ti entre 0 et 1
    res = lambda a,x : 1 - x + math.sin(a*math.pi*x)/(a*math.pi)
    nb_paliers = 2
    return res(2+2*nb_paliers,C.time_range)

#Fonction utilité du client relative au prix p, selon le temps t (jour d'arrivée)
# R ==> [0,1]

def price_utility(C,V):
    pmax = 100
    return max(1-time_decay_utility(C)*V.price/pmax,0)

#Partie déterministe vi(xj) de l'utilité du vol V pour le client C 
# ==> [0,1]
def utility(C,V):
    #Theta est la part représentée par l'utilité horaire vs le prix
    theta = 0.25
    return theta * time_utility(C,V) + (1-theta) * price_utility(C,V)

#Selon une liste de vols Vi flights de longueur n, choix du client C selon loi logit multinomiale
#On définit la variable de choix yi par la PMF
#v0 est l'utilité du choix -1

def choice(C,flights,v0):
    n = len(flights)
    #0 à n-1 pour les n vols et -1 si pas d'achat
    choices = [-1]
    utilities = [v0]
    utilities_exp = [math.exp(v0)]
    for i in range(n):
        flight = flights[i]
        if flight.remaining > 0:
            utilities.append(utility(C,flight))
            utilities_exp.append(math.exp(utility(C,flight)))
            choices.append(i)
    s = sum(utilities_exp)
    
    probabilities = [u/s for u in utilities_exp]
    #print(">>>Le client peut acheter l'un des vols pour les valeurs d'utilité: {} et de probabilité: {}".format(utilities[1:],probabilities[1:]))
    return np.random.choice(choices, 1, p=probabilities)[0]

#proba que le client C choisisse le vol V parmi une liste flights: SEULEMNT SIL  RESTE DES PLACES
#v0 est l'utilité du choix 0
def proba_c_v(C,V,flights,vols_pleins,v0): 
    utilities = [math.exp(v0)]
    for flight in flights:
        if flight not in vols_pleins:
            utilities.append(math.exp(utility(C,flight)))
    s = sum(utilities)
    probability = math.exp(utility(C,V))/s
    return probability

#probabilité de ne chosisir aucun vol
def proba_v0(C,flights,vols_pleins, v0): 
    utilities = [math.exp(v0)]
    for flight in flights:
        if flight not in vols_pleins:
            utilities.append(math.exp(utility(C,flight)))
    s = sum(utilities)
    probability = math.exp(v0)/s
    return probability

