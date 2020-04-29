### TEST DE L'ALGO V1: N clients equirépartis dans le temps

from vol import *
from client import *
from demand import *
from sdp import *
from profit import *
import matplotlib.pylab as plt

### SIMULATEUR D'OFFRE DE VOLS

#Liste des vols
V1 = Vol((8,30),7)
V2 = Vol((16,30),7)
flights = [V1,V2]
#Liste des options de prix possibles
#prices = [0.001,0.01,0.1,1,10,1E2,1E3,1E4,1E5,1E6]
#prices = list(range(100))
prices = [50,55,60,65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 90, 95, 100]
total_seats = sum([f.seats for f in flights])
#v0 
v0 = 3

### SIMULATEUR DE DEMANDE CLIENT SANS REPERE TEMPOREL

N = 15
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
    sales = [] #liste des dico de ventes a chaque expérience. Un dico de vente enregistre les prix de ventes. 
    for k in range(n):
        #On reset les valeurs des attributs des vols:
        for f in flights:
            f.reset()
        prof, dic = profit(flights,prices,list_of_clients,pricing_policy, v0)
        profits.append(prof)
        sales.append(dic)
    print(profits)
    plt.figure(figsize=(8, 6)) 
    for dic in sales:
        lists = sorted(dic.items())
        x, y = zip(*lists)  
        plt.plot(x, y)
    plt.show()
    plt.savefig('img.png') 
    return sum(profits)/n



### OUTPUT
print("Le revenu moyen par place généré par les vols est de {}.".format(simulator(10)/total_seats))
print("La politique de prix est {}".format(pricing_policy))





