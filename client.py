#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import math
import scipy.stats
import random


# Modélisation des clients

class Client:

    def __init__(self,ti):

        #Jour d'arrivée du client normalisée entre 0 et 1
        self.time_range = ti
        #Dans le futur: autres paramètres distinctifs 
        self.fare = "Leisure"
        self.theta = 0.25
        self.temp = 0.05
        self.v0 = 0.5

class Fareclass:

    def __init__(self,name,i0,a,b,theta):

        self.name = name
        #Intensité de la loi NHPP = distribution beta standardisée de paramètres a et b
        self.intensity = lambda x : i0 * scipy.stats.beta.pdf(x,a,b)/x
        # Pondération prix/horaire
        self.theta = theta

    # Simulation d'un processus de poisson non homogène (NHPP) : tirer le nombre de clients arrivés à la date t entre 0 et 1
    def draw_NHPP(self,t):

        return np.random.poisson(self.intensity(t))

### Simulateur de demande

def demand_NHPP(time_horizon,fares):
    """ fonction qui renvoie une liste de clients à d'un horizon temporel de T jours et d'une liste de classes de prix """
    list_of_clients=[]
    #On parcourt les jours de 0 à time_horizon
    for day in range(1,time_horizon+1):

        t = day/time_horizon

        for fare in fares:

            list_fare = []

            for i in range(fare.draw_NHPP(t)):

                c = Client(t)
                c.fare = fare.name
                list_fare.append(c)

            random.shuffle(list_fare)
            list_of_clients += list_fare

    return list_of_clients

def demand_uniform(time_horizon):
    """ fonction qui renvoie une liste de clients à d'un horizon temporel de T jours avec 1 client par jour """

    list_of_clients=[]
    #On parcourt les jours de 0 à time_horizon
    for day in range(1,time_horizon+1):

        t = day/time_horizon
        c = Client(t)
        list_of_clients.append(c)

    return list_of_clients



    


