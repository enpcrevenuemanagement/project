#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy
import math

#Sensibilité au prix selon le temps t (jour)
#Modèle linéaire décroissant variant entre t0=0 et tf
#tf est le nombre de jours d'ouverture de la billetterie, 30 jours par ex

def alpha(t):
    alpha_0=10
    alpha_f=1
    tf=30
    return alpha_0 + t/tf * (alpha_f - alpha_0)

#Utilité relative au prix p selon le temps t (jour)
def price_sensitivity(p,t):
    return math.exp(-alpha(t)*p)

class Client:
    def __init__(self,n):
        """3 attributs à la classe Client : 
            alpha la sensibilité au prix
            time_range l'intervalle de temps où le client arrive
            erreur qui est le bruit de la fonction utilité, dépend uniquement 
            de time_range et mais pas du client et du vol """
        self.time_range = n                 #intervalle de temps où le client arrive. Deux clients différents ont un intervalle de temps différent (injection)
        self.alpha = alpha(self.time_range) #valeur prise arbitrairement, la sensibilité décroit avec le temps


    


