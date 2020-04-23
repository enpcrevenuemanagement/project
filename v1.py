### TEST DE L'ALGO V1: N clients equirépartis dans le temps

from vol import *
from client import *
from demand import *
from sdp import *
from profit import *

### SIMULATEUR D'OFFRE DE VOLS

#Liste des vols
V1 = Vol((12,30),2)
V2 = Vol((18,30),2)
flights = [V1,V2]
#Liste des options de prix possibles
#prices = [0.001,0.01,0.1,1,10,1E2,1E3,1E4,1E5,1E6]
prices = list(range(100))

#v0 
v0 = 10

### SIMULATEUR DE DEMANDE CLIENT SANS REPERE TEMPOREL

N = 4
list_of_clients=[]
for i in range(1,N+1):
    ti = i/N
    C = Client(ti)
    list_of_clients.append(C)

### SDP: POLITIQUE DE PRIX

pricing_policy = SDP(prices, flights, N, v0)[1]

### CALCUL DU PROFIT REALISE
def simulator(n):
    profits = []
    for k in range(n):
        #On reset les valeurs des attributs des vols:
        for f in flights:
            f.reset()
        profits.append(profit(flights,prices,list_of_clients,pricing_policy, v0))
    #print(profits)
    return sum(profits)/n

### OUTPUT

print("Le revenu moyen par place généré par les vols est de {}.".format(simulator(1000)/N))
#print("La politique de prix est {}".format(pricing_policy))
