### TEST DE L'ALGO V1: N clients equirépartis dans le temps

from Vol import *
from Client import *
from demand import *
from sdp import *
from profit import *

### SIMULATEUR D'OFFRE DE VOLS

#Liste des vols
flights = []
#Liste des options de prix possibles
prices = []

### SIMULATEUR DE DEMANDE CLIENT SANS REPERE TEMPOREL

N = 10
list_of_clients=[]
for i in range(1,N+1):
    ti = i/N
    C = Client(ti)
    list_of_clients.append(C)

### SDP: POLITIQUE DE PRIX

pricing_policy = SDP(prices, flights, N)[0]

### CALCUL DU PROFIT REALISE

profit = profit(flights,prices,list_of_clients,pricing_policy)

### OUTPUT

print(profit)