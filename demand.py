### Simulateur de demande

#Compte tenu d'un horizon temporel en nombre de jours N, simule:
#Nombre de clients arrivés chaque jour et leurs préférences

import scipy.stats
import numpy as np

import csv 

from Client import *

#Simulation d'un processus de poisson non homogène (NHPP) 
#pour avoir le nombre de clients arrivés le jour d ie t=d/T
def NHPP(t):
    i0 = 1
    a = 10
    b = 3
    #Distribution beta standardisée de paramètres a et b
    intensity = lambda x : i0 * scipy.stats.beta.pdf(x,a,b)/x
    return np.random.poisson(intensity(t))


def demand_simulator(time_horizon):
    """ fonction qui renvoie list_of_clients, une liste de clients à partir de N, le nombre d'intervalle de temps"""
    list_of_clients=[]
    #On parcourt les jours 1 à time_horizon
    for day in range(1,time_horizon+1):
        t = day/time_horizon
        for k in range(NHPP(t)):
            C = Client(t)
            list_of_clients.append(C)

    with open('client_database', mode='w') as file:
        file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for client in list_of_clients:
            file_writer.writerow([client.time_range])

    return list_of_clients

 