#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  Vol import *
from Client import *
from demand import *

import numpy 
hugeNumber = float("inf")

### LISTE DE VARIABLES GLOBALES DU PROBLEME

time_horizon = 30 #nombre d'intervalles de temps/jours d'ouverture de la billetterie

### SIMULATEUR DE DEMANDE DONNE UN CSV AVEC LA BASE DE CLIENTS

demand_csv(time_horizon)

### SIMULATEUR D'OFFRE DE VOLS