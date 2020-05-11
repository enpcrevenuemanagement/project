import gym
from gym import spaces
import numpy as np

class CustomEnv(gym.Env):
  """Custom Environment that follows gym interface"""
  metadata = {'render.modes': ['human']}

  def __init__(self, flights):
    super(CustomEnv, self).__init__()
    # Define action and observation space
    # They must be gym.spaces objects

    #On stocke flighst pour le modifier au fur et à mesure
    self.flights = flights
    self.K = len(flights)

    # Espace des actions : choix du pricing, (R+)^K
    #La valeur max du prix est la valeur pour laquelle la proba de choix descend en dessous d'un seuil eps
    max_price = 1
    huge = np.inf
    self.action_space = spaces.Box(low = 0, high = max_price, shape=(K,), dtype=np.float32)

    # Espace des observations / états : [0,...,f_K.seats]^K
    self.observation_space = spaces.MultiDiscrete([f.seats for f in flights])

  def step(self, action):
    # Action est un sample de l'espace des actions
    # C'est donc un vecteur de (R+)^K

    self.current_step += 1

    #Boucle pour vérifier qu'on n'excède pas le nombre de clients N qu'on veut simuler
    if self.current_step > N:
    #
 
    #Méthode qui éxécute l'action choisie
    # self._take_action(action)
    #Mettre à jour le prix de chaque vol
    for i in range(self.K):
        self.flights[i].price = action[i]

    #On tire au sort un client
    C = Client()

    #On obtient choice, qui donne l'index du vol choisi ou -1 si pas d'achat
    f_choice = choice(C,self.flights,v0)

    if f_choice != -1:
        #On met à jour flights 
        flights[f_choice].sell()
        reward = action
    else:
        reward = 0

    #On renvoie l'état des places vendues
    observation = [f.seats - f.remaining for f in flights]
    done = (self.current_step == N)

    return observation, reward, done, info
  
  
  def reset(self):

    self.current_step = 0
    for f in flights:
        f.reset()

    observation = [0 for k in range(self.K)]
    observation = [f.seats - f.remaining for f in flights]

    return observation  # reward, done, info can't be included

  def render(self, mode='human'):
      print([f.seats - f.remaining for f in flights])

  def close (self):
    pass