### TEST DE L'ALGO V1: N clients equirépartis dans le temps

from vol import *
from client import *
from utility import *
from sdp import *
from profit import *
import matplotlib.pylab as plt
import numpy as np 

### SIMULATEUR D'OFFRE DE VOLS

#Liste des vols
h1 = Horaire(14,0)
h2 = Horaire(19,0)
V1 = Vol(h1,10)
V2 = Vol(h2,10)
flights = [V1, V2]
#Liste des options de prix possibles
#prices = [0.001,0.01,0.1,1,10,1E2,1E3,1E4,1E5,1E6]
#prices = list(range(100))
prices1 = range(70, 200, 5)
prices2 = range(200, 1000, 50)
prices = np.concatenate((prices1, prices2))
print(len(prices))
total_seats = sum([f.seats for f in flights])

### SIMULATEUR DE DEMANDE CLIENT SANS REPERE TEMPOREL

N = 40
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
    """print(profits)
    plt.figure(figsize=(8, 6)) 
    for dic in sales:
        lists = sorted(dic.items())
        x, y = zip(*lists)  
        plt.plot(x, y)
    plt.show()
    plt.savefig('img.png')"""
    return sum(profits)/n



### OUTPUT
print("Le revenu moyen par place généré par les vols est de {}.".format(simulator(10)/total_seats))
print("La politique de prix est {}".format(pricing_policy))





