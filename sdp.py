from  Vol import *
from Client import *
import numpy 
hugeNumber = float("inf")

#EXEMPLE AVEC 2 VOLS DE 2 PLACES CHACUNS AVEC 3 PRIX POSSIBLES PAR PLACE SUR 4 CLIENTS
N = time_horizon = 4 #nombre d'intervalles de temps/jours d'ouverture de la billetterie
#vols_de_la_journée =  [v1,v2]  liste de 2 vols de 2 places chacuns dans cet exemple
#définition des états : chaque état est la liste des vecteurs v.sold possibles (sans le prix du coup)
#Il faudrait créer un attribut v.sold_price qui prend en compte le prix de vente de chaque vol pour le stocker
prices = [10,30,100] #les prix possibles pour chaque vol, 3 dans cet exemple

#constructeur bourrin des états possibles avec le vecteur prices et 2 vols de 2 places chacuns(j'ai pas trouvé plus simple...)
#Julian est en train de refaire ce constucteur sans prendre en compte le prix des places de manière plus clean 
states = []
for i in prices:
    for j in prices:
        states.append([[i],[j]])
        states.append([[i],[]])
        states.append([[],[j]])
        states.append([[],[i,j]])
        states.append([[i,j],[]])
        states.append([[],[]])
        for k in prices:
            states.append([[i,j],[k]])
            states.append([[i],[j,k]])
            for l in prices:
                states.append([[i,j],[k,l]])
for k in states: #on retire les doublons
        c=states.count(k)
        if c>1:
            states.remove(k)
 
#définition du pricing : chaque pricing est un vecteur de prix (1 prix par vol) [p1,p2]
pricing_options = []
for i in prices:
    for j in prices:
        if [i,j] not in pricing_options:
            pricing_options.append([i,j])

#matrice f où on stock le gain futur maximal (espérance) f[i][j] si on est dans l'état j au pas de temps i
f = [[0 for k in range(len(states))] for l in range(N+1)]  
#matrice x de la même taille où on stock la décision de pricing optimale associée à ce gain f[i][j]
#autrement dit il faut prendre la décision x[i][j] si on est dans l'état j à i, et alors le gain maximal 
#qu'on pourra espérer avoir à la fin est f[i][j]
x = [[[0,0] for k in range(len(states))] for l in range(N+1)]  

#Debut de l'algorithme, cf les slides du CERMICS pour plus de détails
 
for t in reversed(range(N)) : #nouvelle étape, on est en backward (à parcourir à l'envers)
    for i in states:  #états accessibles à l'étape t, toutes les paires possibles de vecteur sold
        value = -hugeNumber 
        bestMove = [] 
        for d in pricing_options :  #decision du nouveau pricing pour chacun des 2 vols [30,30] [30,50] [50,50] ....
            esp = 0
            for r in range(2) : #le client choisi son vol en maximisant son utilité ou pas de vol, 0 = pas de vol, 1=v1 et 2=v2
                if r == 0: #s'il ne choisi pas de vol on reste dans le même état i 
                    state = i
                    esp += (proba que le client choisisse pas de vol)*0 + f[t+1][states.index(state)] #le bénéfice associé à ce cas de figure est nul
                else : #il choisit le vol 1 ou 2
                    state = i
                    state.append(d[r-1]) #on passe dans un nouvel état : celui qui correspond à la vente d'une place de plus au prix d[r-1] sur le vol r
                    esp += (proba que le client choisisse ce vol)*d[r-1] + f[t+1][states.index(state)] #le bénéfice associé à ce cas de figure est d[r-1]
#nécessité de passer en backward : des qu'on calcule le nouvel état qui correspond à l'issue de la vente on doit savoir quel est le resultat de l'espérance
#des gains de ce nouvel état de t+1 à n pour calculer l'espérance de gains globale de t à n.
            if esp > value :  
                value = esp
                bestMove = d   #si l'esperance de gain est maximale pour une decision de pricing, on stock la valeur et la decision associée

        #on stock à l'étape t et à l'état i la fonction valeur bénéfice dans f et la décision de pricing dans x
        f[t][states.index(i)] = value
        x[t][states.index(i)] = bestMove

    # fin boucle states i
# fin boucle stages t
 
#EBAUCHE DE SIMULATEUR UN PEU A L'ARRACHE MAIS IMPORTANT CAR LE FRAMEWORK Y EST A MON SENS
#Maintenant il faut établir le simulateur : se donner un set de vol et de client et simuler les décisions de chaque clients à chaque étape
from demand import *
from Client import *
from time import *
from utility import *
from Vol import *

#bug sur le generateur de clients, je le fait à la main 
clients = [Client(0), Client(1), Client(2), Client(3)] #4 clients 
vols = [Vol(3,2), Vol(7,2)]    #2 vols de 2 places, 1 le matin et 1 l'aprem 

vols[0].price = x[0][f[0].index(max(f[0]))][0] #pricing initial sur les vols 
vols[1].price = x[0][f[0].index(max(f[0]))][1]

state = [[],[]] #état initial, à modifier en fonction de ce que code Julian 

for t in range(1,N):
    choice(clients[t-1], vols, 0.2).sold.append(choice(clients[t-1], vols, 0.2).price) #on ajoute le prix au vecteur sold auquel le billet a été vendu au client 
    state = [vols[0].sold, vols[1].sold]
    #nouveau pricing : la on a juste à parcourir la matrice x des pricing optimaux
    #le code est à travailler pour ce simulateur
    #je n'ai pas pris en compte le cas d'arret si il n'y a plus de place dans un vol, à examiner (rajouter dans SDP ? dans simulateur ?)
    vols[0].price = x[t][states.index(state)][0]
    vols[1].price = x[t][states.index(state)][1]
    print("state : " + state)
    print("nouveau pricing :" + x[t][states.index(state)])