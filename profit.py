import csv 

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

def profit(flights,prices,list_of_clients,pricing_policy):

    #Si on a trop de clients, la politique de prix est invalide ==> ERREUR
    N = len(list_of_clients)

    #Sinon on prend les clients par ordre d'arrivée

    #Initialisation
    step = 0
    #Liste des états
    states = States(flights)
    #Etat initial (0,0,....,0)
    state = states[0]

    for client in list_of_clients:
        #On cherche le pricing correspondant (dico)
        pricing = x[step][state]
        #On doit mettre à jour le prix proposé de chaque vol
        for price in pricing:
            break
            #flights[i]  prend le prix pricing[i]

        #On regarde sa réaction 
        #flight_choice = 0 si pas d'achat, i si achat vol i

        #QUESTION: Flights doit contenir les vols encore dispo?

        flight_choice = choice(client,flights,v0)

        #Si achat
        if flight_choice != 0:
            #Mettre a jour les places restantes
            state = 

        #si pas d'achat rien ne change

        step += 1








