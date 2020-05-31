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
        #Type de client
        self.fare = "Leisure"
        #Température pour le softmax pour ce type
        self.temp = 0.01
        #Utilité du choix zéro pour ce type
        self.v0 = 0.2

    def theta(self):
        # Renvoie une sensibilité au prix entre start et final en focntion de ti entre 0 et 1
        # Sensibilité au prix avec les 2 paliers comme axel nous a montré
        # [0,1] ==> [0,1]
        nb_paliers = 2
        #Theta touriste
        start = 0.9
        #Theta business
        final = 0.1

        res = lambda a,x : start + (start - final) * (math.sin(a*math.pi*x)/(a*math.pi) - x)
        
        return res(2+2*nb_paliers,self.time_range)

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
    #On parcourt les jours de 1 à time_horizon
    for day in range(0,time_horizon+1):

        t = day/time_horizon
        c = Client(t)
        list_of_clients.append(c)

    return list_of_clients


    


