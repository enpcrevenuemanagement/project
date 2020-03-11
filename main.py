#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  Vol import *
from Client import *

#Definition des horaires des vols

class Time:

    def init(self,h,m):
        self.hours=h+m/60
        self.minutes=h*60+m

#Exemple d'instances pour l'horaire:
t1 = Time(8,30) #8h30
t1 = Time(12,30) #12h30



def utility(C,V):
    """fonction qui définit l'utilité du vol V pour le client C
    fonction scalaire linéaire au prix et non linéaire en fonction de l'heure du vol"""
    return C.alpha + V.time_utility + C.erreur #le terme p(i,j) manque