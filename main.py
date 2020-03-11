#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  Vol import *
from Client import *

#Definition des horaires des vols

class Time:

    def init(self,h,m):
        self.hours=h+m/60
        self.minutes=h*60+m

#Exemple d'instance pour l'horaire: 12h30
t1 = Time(12,30)


def utility(C,V):
    """fonction qui définit l'utilité du vol V pour le client C
    fonction scalaire linéaire au prix et non linéaire en fonction de l'heure du vol"""
    return C.alpha + V.time_utility + C.erreur #le terme p(i,j) manque