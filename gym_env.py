import gym
from gym import spaces
import numpy as np

from client import *
from vol import *
from utility import *

class RMenv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, flights, N):
    super(RMenv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects

    #On stocke flights pour le modifier au fur et à mesure
    self.flights = flights
    self.K = len(flights)

    # Nombre de clients par épisode
    self.N = N

    # Utilité du choix -1
    self.v0 = 1

    # Espace des actions : choix du pricing, (R+)^K
    # La valeur max du prix est la valeur pour laquelle la proba de choix descend en dessous d'un seuil eps
    max_price = 1E4
    huge = np.inf
    self.action_space = spaces.Box(low = 1E3, high = max_price, shape=(self.K,), dtype=np.float32)

    # Espace des observations / états : [0,...,f_K.seats]^K
    self.observation_space = spaces.MultiDiscrete([f.seats for f in flights])

    #On stocke le pricing modifié au fur et à mesure pour l'étape render
    self.pricing = []
    

  def step(self, action):
    # Action est un sample de l'espace des actions
    # C'est donc un vecteur de (R+)^K

    self.current_step += 1

    # On met à jour le pricing pour l'étape render
    self.pricing = action

    #Méthode qui éxécute l'action choisie ?
    # self._take_action(action)

    #Mettre à jour le prix de chaque vol
    for i in range(self.K):
      #print(action)
      self.flights[i].price = action[i]

    #On tire au sort un client
    ti = i / self.N
    C = Client(ti)

    #On obtient choice, qui donne l'index du vol choisi ou -1 si pas d'achat
    try:
      f_choice = choice(C,self.flights,self.v0)
    except:
      # Si erreur 
      f_choice = -1
      print("Erreur de calcul du choix client pour le pricing suivant: {}".format(action))
      exit()

    if f_choice != -1:
        #On met à jour flights 
        self.flights[f_choice].sell()
        reward = float(action[f_choice])
    else:
        reward = 0

    #On renvoie l'état des places vendues
    observation = np.array([f.seats - f.remaining for f in self.flights])
    done = (self.current_step == self.N)

    info = {"info 1": "Pas d'info"}

    return observation, reward, done, info
  
  
  def reset(self):
    """
    Important: the observation must be a numpy array
    :return: (np.array) 
    """

    self.current_step = 0
    for f in self.flights:
        f.reset()

    observation = np.array([0 for k in range(self.K)])

    return observation  # reward, done, info can't be included

  def render(self, mode='human'):
      print("Remplissage {}".format([f.seats - f.remaining for f in self.flights]))
      print("Pricing {}".format(self.pricing))

  def close (self):
    pass