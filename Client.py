#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import math

#Modélisation des caractéristiques DETERMINISTES propres à chaque client (jour d'arrivée, catégorie de client...)
#Cela exclut tout ce qui dépend aussi du vol (utilité du client pour le vol entre autres ==> utility.py)
#Cela exclut donc aussi le stockage en attribut de la réalisation de la variable aléatoire de l'aléa du client
#L'aléa lié au client est pris en compte dans la loi logit multinomiale

class Client:

    def __init__(self,n):
        #Jour d'arrivée du client
        self.time_range = n  


    


