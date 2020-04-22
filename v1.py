### TEST DE L'ALGO V1: N clients equirépartis dans le temps

from vol import *
from client import *
from demand import *
from sdp import *
from profit import *

### SIMULATEUR D'OFFRE DE VOLS

#Liste des vols
V1 = Vol((12,30),4)
V2 = Vol((18,30),4)
flights = [V1,V2]
#Liste des options de prix possibles
prices = [20,30,40]

### SIMULATEUR DE DEMANDE CLIENT SANS REPERE TEMPOREL

N = 10
list_of_clients=[]
for i in range(1,N+1):
    ti = i/N
    C = Client(ti)
    list_of_clients.append(C)

### SDP: POLITIQUE DE PRIX

pricing_policy = SDP(prices, flights, N)[1]

### CALCUL DU PROFIT REALISE
flights = [V1,V2]
profit = profit(flights,prices,list_of_clients,pricing_policy)

### OUTPUT

print("Le profit total généré par les vols {} est de {}.".format(flights,profit))