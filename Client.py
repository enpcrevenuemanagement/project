#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy

class Client:
    def __init__(self):
        """3 attributs à la classe Client : 
            alpha la sensibilité au prix
            day le jour d'arrivée, qui est le nombre de jours avant le vol
            erreur qui est le bruit de la fonction utilité, dépend uniquement 
            du temps et mais pas du client et du vol """
        self.alpha = -1 #valeur prise arbitrairement, la sensibilité 
        #décroit avec le temps
        self.day = numpy.random.randint(1,10) #on se place pour l'instant sur 
        #un horizon de 10 jours et on tire aléatoirement le jour d'arrivée
        self.erreur = 0
    
    
    def gumbel(self):
        """Donne à l'erreur du client une valeur aléatoire selon une loi de 
        Gumbel de paramètre 0 et 10-self.day
        0 est le paramètre de position
        10-self.day est le paramètre d'étalement
        l'erreur dépend uniquement du temps"""
        self.erreur = numpy.random.gumbel(0, 11-self.day) #l'erreur est 
        #d'autant plus grande que le vol est dans longtemps (i.e d'autant 
        #plus que  day est petit) 


    


