import csv 
from vol import *
from utility import *

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
def state_index(state):
    return int(sum([state[i]*np.prod(seats[i+1:]) for i in range(len(flights))]))

def profit(flights,prices,list_of_clients,pricing_policy):

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
        #On cherche le pricing correspondant (dico)
        #PB : state index ???
        pricing = x[step][state_index]
        #On doit mettre à jour le prix proposé de chaque vol
        for price in pricing:
            break
            #flights[i]  prend le prix pricing[i]

        #On regarde sa réaction 
        #flight_choice = -1 si pas d'achat, i si achat vol i

        #QUESTION: Flights doit contenir les vols encore dispo?

        flight_choice = choice(client,flights,v0)

        #Si achat
        if flight_choice != -1:
            flight = flights[flight_choice]
            #On modifie l'objet Vol pour 
            flight.sell()
            #On modifie l'état
            state[flight] = flight.remaining
            #On est obligé de chercher l'index dans states.....????
            state_index = states.index(state)

        #si pas d'achat rien ne change
        step += 1

    #Quand on a fini de parcourir la file de clients, on calcule le gain total
    return sum([f.profit for f in flights])








