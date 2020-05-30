import tensorflow as tf

from stable_baselines.ddpg.policies import MlpPolicy
from stable_baselines.common.noise import NormalActionNoise, OrnsteinUhlenbeckActionNoise, AdaptiveParamNoiseSpec
from stable_baselines import DDPG

#Importer les autre scripts
from gym_env import *
from vol import *

# Initialisation des vols

h1 = Horaire(14,0)
h2 = Horaire(19,0)

V1 = Vol(h1,10)
V2 = Vol(h2,10)

flights = [V1]

# horizon temporel (longueur d'un épisode = nombre de clients si demande equirepartie)
T = 10

# Range d'exploration du prix
max_price = 200

# On construit l'environnement Gym
env = RMenv(flights, T, max_price, verbose = 0)
# On donne le constructeur de l'environnement Gym
env_fn = lambda : env

# the noise objects for DDPG
n_actions = env.action_space.shape[-1]
param_noise = None
action_noise = OrnsteinUhlenbeckActionNoise(mean=np.zeros(n_actions), sigma=float(0.5) * np.ones(n_actions))

model = DDPG(MlpPolicy, env, verbose=1, param_noise=param_noise, action_noise=action_noise)
model.learn(total_timesteps=400000)
model.save("ddpg_mountain")

del model # remove to demonstrate saving and loading

model = DDPG.load("ddpg_mountain")

while True:
    obs = env.reset()
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
