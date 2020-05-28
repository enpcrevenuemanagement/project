import tensorflow as tf
import spinup

#Importer les autre scripts
from gym_env import *
from vol import *

# Initialisation des vols

h1 = Horaire(14,0)
h2 = Horaire(19,0)

V1 = Vol(h1,10)
V2 = Vol(h2,10)

flights = [V2]

# Nombre de clients dans la file = horizon temporel (longueur d'un épisode)
T = 20
max_price = 100

# On construit l'environnement Gym

# If the environment don't follow the interface, an error will be thrown
from stable_baselines.common.env_checker import check_env
env = RMenv(flights, T, max_price)
check_env(env, warn=True)

# On donne le constructeur de l'environnement Gym
env_fn = lambda : env

# On run l'algo
spinup.ddpg_tf1(env_fn, ac_kwargs={}, steps_per_epoch=4000, epochs=100, replay_size=1000000, gamma=0.99, polyak=0.995, 
pi_lr=0.001, q_lr=0.001, batch_size=100, start_steps=10000, update_after=1000, update_every=50, 
act_noise=0.1, num_test_episodes=1, max_ep_len=1000, logger_kwargs={}, save_freq=1)