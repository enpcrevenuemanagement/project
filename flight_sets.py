from vol import *
from client import *
from utility import *

from scipy.optimize import minimize_scalar

h1 = Horaire(14,0)
h2 = Horaire(19,0)

V1 = Vol(h1,14)
V1.price = 102

V2 = Vol(h2,5)
V2.price = 100

flights = [V1]

T = Client(0)
B = Client(1)

C = B

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

def fn(p):
    hor = lambda h : math.exp(-1/12*(h-9)**2) + math.exp(-1/12*(h-19)**2)
    uh = hor(14)

    price_scale = 100
    prix = lambda p : 1 - p / price_scale

    theta = 0.1
    ut = theta * prix(p) + ( 1 - theta ) * uh

    return np.exp(ut/0.01) / ( np.exp(0.2/0.01) + np.exp(ut/0.01) )

def fn_opt(p):
    return -p*fn(p)

opt = minimize_scalar(fn_opt, bounds=[0,200], method='bounded')
print("Optimum price = {}".format(opt.x))
print("Esp = {}".format(-fn_opt(opt.x)))



