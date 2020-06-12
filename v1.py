### TEST DE L'ALGO V1: N clients equirépartis dans le temps

from vol import *
from client import *
from utility import *
from sdp import *
from profit import *
from plot import *

import matplotlib.pylab as plt
import numpy as np 
import seaborn as sns
import pandas as pd

### SIMULATEUR D'OFFRE DE VOLS

#Liste des vols
h1 = Horaire(8,0)
h2 = Horaire(14,0)
h3 = Horaire(19,0)
V1 = Vol(h1,15)
V2 = Vol(h2,75)
V3 = Vol(h3,10)
flights = [V2]
#Liste des options de prix possibles
#prices = [0.001,0.01,0.1,1,10,1E2,1E3,1E4,1E5,1E6]
#prices = list(range(100))
prices1 = range(70, 200, 5)
prices2 = range(200, 1000, 50)
prices = np.concatenate((prices1, prices2))

total_seats = sum([f.seats for f in flights])

### SIMULATEUR DE DEMANDE CLIENT SANS REPERE TEMPOREL

N = 140
list_of_clients = demand_uniform(N)

### SDP: POLITIQUE DE PRIX

pricing_policy = SDP(prices, flights, N)[1]

### CALCUL DU PROFIT REALISE
def simulator(n):
    profits = []
    sales = [] #liste des dico de ventes a chaque expérience. Un dico de vente enregistre les prix de ventes. 
    for k in range(n):
        #On reset les valeurs des attributs des vols:
        for f in flights:
            f.reset()
        prof, dic = profit(flights,prices,list_of_clients,pricing_policy)
        profits.append(prof)
        sales.append(dic)
    profits_par_place = [k/total_seats for k in profits]
    standard_dev = np.std(profits_par_place)
    return sum(profits)/n, sales


### OUTPUT
profit_par_exp, sales = simulator(100) 
print("Le revenu moyen par place généré par les vols est de {}.".format(profit_par_exp/total_seats))
print("La politique de prix est {}".format(pricing_policy))
#plotting
plot_remplissage_ventes(sales, 75) 
 