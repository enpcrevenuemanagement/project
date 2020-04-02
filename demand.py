

### Simulateur de demande
#Compte tenu d'un horizon temporel en nombre de jours N, simule:
#Nombre de clients arrivés chaque jour

import scipy.stats
import numpy as np

from Client import *

time_horizon = 30

#Simulation d'un processus de poisson non homogène (NHPP) 
#pour avoir le nombre de clients arrivés le jour t sur un horizon de taille N
def NHPP(t,time_horizon):
    i0 = 1
    a = 1
    b = 1
    #Distribution beta standardisée de paramètres a et b
    intensity = lambda x : i0 * scipy.stats.beta.pdf(x,a,b)/x
    return np.random.poisson(intensity(t/time_horizon))


def demand_simulator(time_horizon):
    """ fonction qui renvoie list_of_clients, une liste de clients à partir de N, le nombre d'intervalle de temps"""
    list_of_clients=[]
    for day in range(time_horizon):
        for k in range(NHPP(day,time_horizon)):
            C = Client(k)
            list_of_clients.append(C)
    return list_of_clients

 