#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  Vol import *
from Client import *
from demand import *
from sdp.py import *

import numpy 
hugeNumber = float("inf")

### SIMULATEUR D'OFFRE DE VOLS

#Liste des vols
flights = []
#Liste des options de prix possibles
prices = []

### SDP: POLITIQUE DE PRIX

#Rappel: politique de prix = matrice x 
#Décisions x[i][j] si on est dans l'état j à i
#x[i][j] est un pricing (liste)

#Nombre de clients N à fixer pour le calcul ==> PROBLEME
N = 4
pricing_policy = SDP(prices, flights, N)[0]

### SIMULATEUR DE DEMANDE DONNE UN CSV AVEC LA BASE DE CLIENTS

#nombre d'intervalles de temps/jours d'ouverture de la billetterie
time_horizon = 30 
list_of_clients = demand_simulator(time_horizon)

### CALCUL DU PROFIT REALISE
profit = profit(flights,prices,list_of_clients,pricing_policy)



