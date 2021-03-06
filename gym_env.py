import gym
from gym import spaces
import numpy as np

from client import *
from vol import *
from utility import *

class RMenv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, flights, T, max_price, verbose = 0):
    super(RMenv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects

    self.verbose = verbose

    # Horizon temporel
    self.T = T

    #On stocke flights pour le modifier au fur et à mesure de l'épisode
    self.flights = flights
    self.K = len(flights)
    self.total_seats = sum([f.seats for f in self.flights])
    #On stocke le pricing modifié au fur et à mesure pour l'étape render
    self.pricing = []
    # max price 
    self.max_price = max_price

    # Liste des clients pour l'épisode en cours, à tirer dans la méthode reset
    self.demand = demand_uniform(self.T)
    # Nombre de clients
    self.N = len(self.demand)

    #current step 
    self.current_step = 0 
    #dernier choix effectué
    self.last_choice = "NA"

    # Espace des actions : choix du pricing, (R+)^K normalisé
    self.action_space = spaces.Box(low = -1, high = 1, shape=(self.K,), dtype=np.float32)
    # Espace des observations / états : [0,...,f_K.seats]^K
    self.observation_space = spaces.MultiDiscrete([f.seats for f in flights])
  
  def full(self):
    res = True

    for f in self.flights:
      if f.remaining > 0:
        res = False
    return res


  def get_choice(self,pricing):
    #Avancer dans la liste de clients et sortir un choix
    if self.verbose == 1:
      print(">>> Pricing proposé : {}".format(pricing))

    #Mettre à jour le prix de chaque vol
    for j in range(self.K):
      self.flights[j].price = pricing[j]

    #On tire un client à partir de la liste donnée pour l'épisode
    try:
      C = self.demand[self.current_step]
      f_choice = choice(C,self.flights,self.verbose)
    except:
      print("Choice error for client {} in list of {} clients".format(self.current_step+1,self.N))
      f_choice = -1

    if f_choice != -1:
        #On met à jour flights 
        self.flights[f_choice].sell()
        reward = float(pricing[f_choice])
    else:
        reward = 0

    if self.verbose == 1:
      print(">>> Choix : {}".format(f_choice))
      print(">>> Gain : {}".format(reward))
      print(">>> Gain total épisode en cours : {}".format( sum( [f.gain() for f in self.flights]) ))
      print(">>> Remplissage {}".format([f.seats - f.remaining for f in self.flights]))

    #On obtient choice, qui donne l'index du vol choisi ou -1 si pas d'achat
    return f_choice, reward


  def step(self, action):

    # Action est la valeur du pricing choisi entre -1 et 1
    pricing = (1+action)*self.max_price/2
    # On met à jour le pricing pour l'étape render
    self.pricing = pricing

    if self.verbose == 1:
      print("Client {} sur {}".format(self.current_step+1,self.N))

    f_choice, reward = self.get_choice(self.pricing)

    self.last_choice = f_choice

    self.current_step += 1

    #On renvoie l'état des places vendues
    observation = np.array([f.seats - f.remaining for f in self.flights])
    #On termine au bout de la file de clients
    done = (self.current_step >= self.N) or self.full()
    info = {"Choix": f_choice , "Prix": reward}

    # Rescale reward ???
    reward = reward / (self.max_price*self.total_seats)

    return observation, reward, done, info

  def reset(self):
    """
    Important: the observation must be a numpy array
    :return: (np.array) 
    """
    #C'est l'état de l'environnement au début d'un épisode

    self.current_step = 0

    for f in self.flights:
        f.reset()
      
    self.demand = demand_uniform(self.T)
    self.N = len(self.demand)

    observation = np.array([0 for k in range(self.K)])

    return observation
  
  
  def render(self, mode='human'):
      print("Current step = {}".format(self.current_step-1))
      print(">>> Pricing proposé = {} pour un prix max de {}".format(self.pricing,self.max_price))
      print(">>> Choix effectué = {}".format(self.last_choice))
      print(">>> Remplissage = {}".format([f.seats - f.remaining for f in self.flights]))

  def close (self):
    pass