#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  Vol import *
from Client import *

#Definition des horaires des vols

class time:

    def init(self,h,m):
        self.hours=h
        self.minutes=m

    def convert_to_hour(self):
        return self.hours+self.minutes/60


def utility(C,V):
    """fonction qui définit l'utilité du vol V pour le client C
    fonction scalaire linéaire au prix et non linéaire en fonction de l'heure du vol"""
    return C.alpha + V.time_utility + C.erreur #le terme p(i,j) manque