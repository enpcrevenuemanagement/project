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
            day le jour d'arrivée 
            erreur qui est le bruit de la fonction utilité, dépend uniquement 
            du temps et mais pas du client et du vol """
        self.day = n                 #jour d'arrivée du client, qui est unique pour chaque client et chaque client arrive un jour (bijection)
        self.alpha = alpha(self.day) #valeur prise arbitrairement, la sensibilité décroit avec le temps
        self.erreur = 0              #le bruit du client
    
    
    def gumbel(self):
        """Donne à l'erreur du client une valeur aléatoire selon une loi de 
        Gumbel de paramètre 0 et 10-self.day
        0 est le paramètre de position
        10-self.day est le paramètre d'étalement
        l'erreur dépend uniquement du temps"""
        self.erreur = numpy.random.gumbel(0, 11-self.day) #l'erreur est 
        #d'autant plus grande que le vol est dans longtemps (i.e d'autant 
        #plus que  day est petit) 


    


