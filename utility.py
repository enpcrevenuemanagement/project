### MODELES DE PREFERENCES
import numpy as np
import math

from vol import *
from horaire import *
from client import *

#Fonction utilité du client relative à l'horaire h du vol (chameau)
#Fonction entre 0 et 1

def time_utility(C,V):
    #Prend en entrée l'horaire normalisé dans la journée (cf classe Horaire)
    res = lambda h : (5 + math.cos(h-8) - (h-8)*math.cos(h-8))/12.3507
    return res(V.departure_time.hours)

#Fonction avec les 2 paliers comme axel nous a montré
# [0,1] ==> [0,1]

def time_decay_utility(C):
    #Prend en entrée un entier qui code le jour d'arrivée du client entre 1 et time_horizon
    res = lambda a,x : 1 - x + math.sin(a*math.pi*x)/(a*math.pi)
    return res(3,C.time_range)

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
#v0 est l'utilité du choix -1

def choice(C,flights,v0):
    n = len(flights)
    #0 à n-1 pour les n vols et -1 si pas d'achat
    choices = [-1]
    utilities = [math.exp(v0)]
    for i in range(n):
        flight = flights[i]
        #Le client ne choisit que parmi les vols ou il reste des places !!!
        if flight.remaining > 0:
            utilities.append(math.exp(utility(C,flight)))
            choices.append(i)
    s = sum(utilities)
    print(">>>Le client peut acheter l'un des vols pour les valeurs d'utilité suivantes: {}".format(utilities[1:]))
    probabilities = [u/s for u in utilities]
    return np.random.choice(choices, 1, p=probabilities)[0]

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

