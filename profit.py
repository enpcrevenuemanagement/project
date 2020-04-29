import csv 
from vol import *
from utility import *
from sdp import *

def seat_available(flights):
    for f in flights:
        if f.remaining > 0:
            return True
    return False

def profit(flights,prices,list_of_clients,pricing_policy,v0):

    #Si on a trop de clients, la politique de prix est invalide ==> ERREUR
    N = len(list_of_clients)
    

    #Sinon c'est OK et on prend les clients par ordre d'arrivée
    #Remarque : si on a pas assez de clients, la politique de prix sera certainement sous-optimale

    #Initialisation
    step = 0
    #Liste des états
    states = States(flights)
    #Etat initial (0,0,....,0)
    state_index = 0
    dic_sales = {}
    count = 0
    for client in list_of_clients:
        state = states[state_index]

        print("Arrivée du client n°{} sur {}".format(step+1,N))

        if seat_available(flights) == False:
            print("Plus de siège disponible, plus d'achat.")
            break
        else:
            available = [f.remaining for f in flights]
            print("Sièges disponibles : {}".format(available))

        #S'il reste des sièges on cherche le pricing correspondant [p1,...,pn]
        pricing = pricing_policy[step][state_index]
        print(">>>Pricing proposé :{}".format(pricing))
        #On doit mettre à jour le prix proposé de chaque vol
        for i in range(len(flights)):
            flights[i].price = pricing[i]

        #Le client prend une décision
        #flight_choice = -1 si pas d'achat, i si achat vol i
        #Choix seulement s'il reste de la place !
        flight_choice = choice(client,flights,v0)

        #Si achat
        if flight_choice != -1:
            flight = flights[flight_choice]
            #print(">>>Le client choisit le vol {} d'utilité {}".format(flight_choice,math.exp(utility(client,flights[flight_choice]))))
            u = utility(client,flight)
            print(">>>Le client choisit le vol {} pour un prix de {} et une utilité de {}".format(flight_choice,flight.price,u))
            dic_sales[count] = flight.price
            count+=1
            
            #On modifie l'objet Vol pour 
            flight.sell()
            
            #On récupère l'index du nouvel état
            new_state = state.copy()
            new_state[flight] =  flight.seats - flight.remaining
            state_index = states.index(new_state)

        else:
            print(">>>Le client choisit de ne pas acheter pour une utilité de {}".format(v0))


        #si pas d'achat rien ne change
        step += 1
    #Quand on a fini de parcourir la file de clients, on calcule le gain total
    return sum([f.gain() for f in flights]), dic_sales








