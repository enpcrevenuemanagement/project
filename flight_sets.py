from vol import *
from client import *
from utility import *

h1 = Horaire(14,0)
h2 = Horaire(19,0)

V1 = Vol(h1,14)
V1.price = 500

V2 = Vol(h2,5)
V2.price = 100

flights = [V1]

T = Client(0)
B = Client(1)

C = T

for f in flights:
    print("Vol")
    print(">>> Time utility = {}".format(time_utility(C,f)))
    print(">>> Price utility = {}".format(price_utility(C,f)))
    print(">>> Utility = {}".format(utility(C,f)))
    print(">>> Utility / temp = {}".format(utility(C,f)/C.temp))
print("Overall")
print(">>> Choix : {}".format(choice(C,flights,1)))

f = Fareclass("Leisure",1,2,3,0.5)

fares = [f]

list = demand_NHPP(10,fares)




