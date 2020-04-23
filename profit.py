import csv 
from vol import *
from utility import *
from sdp import *

### READ CSV DATABASE CLIENT ==> LISTE DE CLIENTS (OBJETS)
'''with open('client_database') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                line_count += 1
        print(f'Processed {line_count} lines.')

    return list_of_clients'''


#Fonction pour trouver l'index dans states à partir d'un state en remplacement d'une recherche d'index
def find_index(state,flights):
    seats = [flight.seats for flight in flights]
    return int(sum([state[flights[i]]*np.prod(seats[i+1:]) for i in range(len(flights))]))

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
    state = states[state_index]



    for client in list_of_clients:
        print("Arrivée du client n°{} sur {}".format(step+1,N))
        #On cherche le pricing correspondant [p1,...,pn]
        pricing = pricing_policy[step][state_index]
        print(">>>Les prix proposés sont :{}".format(pricing))
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
            #On modifie l'objet Vol pour 
            flight.sell()
            #On modifie l'état
            state[flight] = flight.remaining
            #On récupère l'index
            state_index = find_index(state,flights)

        else:
            print(">>>Le client choisit de ne pas acheter pour une utilité de {}".format(v0))


        #si pas d'achat rien ne change
        step += 1

    #Quand on a fini de parcourir la file de clients, on calcule le gain total
    return sum([f.gain() for f in flights])








