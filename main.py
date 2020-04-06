#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from  Vol import *
from Client import *
from demand import *

import numpy 
hugeNumber = float("inf")

### SIMULATEUR DE DEMANDE DONNE UN CSV AVEC LA BASE DE CLIENTS

time_horizon = 30 #nombre d'intervalles de temps/jours d'ouverture de la billetterie
database_clients = demand_simulator(time_horizon)

### SIMULATEUR D'OFFRE DE VOLS

database_vols = []

### SDP

pricing_policy = sdp(database_clients,database_vols)