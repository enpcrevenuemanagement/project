from vol import *
from client import *
from utility import *

h = Horaire(19,0)
V = Vol(h,5)

C = Client(0)

print("Time utility = {}".format(time_utility(C,V)))
print("Price utility = {}".format(price_utility(C,V)))
print("Utility = {}".format(utility(C,V)))

f = Fareclass("Leisure",1,2,3,0.5)

fares = [f]

list = demand_NHPP(10,fares)

print(list)
print(len(list))




