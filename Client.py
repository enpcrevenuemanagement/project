#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy

a0 = 1
k = 0.1
alpha = lambda d : a0 - k*d

class Client:
    def __init__(self,n):
        """3 attributs à la classe Client : 
            alpha la sensibilité au prix
            time_range l'intervalle de temps où le client arrive
            erreur qui est le bruit de la fonction utilité, dépend uniquement 
            de time_range et mais pas du client et du vol """
        self.time_range = n                 #intervalle de temps où le client arrive. Deux clients différents ont un intervalle de temps différent (injection)
        self.alpha = alpha(self.time_range) #valeur prise arbitrairement, la sensibilité décroit avec le temps
        self.erreur = 0                     #le bruit du client
    
    
    def gumbel(self):
        """Donne à l'erreur du client une valeur aléatoire selon une loi de 
        Gumbel de paramètre 0 et 1
        0 est le paramètre de position
        1 est le paramètre d'étalement"""
        self.erreur = numpy.random.gumbel(0, 1)


    


