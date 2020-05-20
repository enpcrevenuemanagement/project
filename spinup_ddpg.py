import tensorflow as tf
import spinup

#Importer les autre scripts
from gym_env import *
from vol import *

# Initialisation des vols
V1 = Vol((10,30),5)
V2 = Vol((12,30),5)
V3 = Vol((14,30),5)
V4 = Vol((16,30),5)
V5 = Vol((18,30),5)
flights = [V1,V2,V3]

# Nombre de clients dans la file (longueur d'un épisode)
N = 20

# On construit l'environnement Gym

# If the environment don't follow the interface, an error will be thrown
from stable_baselines.common.env_checker import check_env
env = RMenv(flights, N)
check_env(env, warn=True)

# On donne le constructeur de l'environnement Gym : méthode 1
env_fn = lambda : env

# On donne le constructeur de l'environnement Gym : méthode 2 avec un vectorized env
from stable_baselines.common.cmd_util import make_vec_env
env_fn2 = lambda : make_vec_env(lambda: env, n_envs=1)

# On run l'algo
spinup.ddpg_tf1(env_fn, ac_kwargs={}, 
seed=0, steps_per_epoch=4000, epochs=10, replay_size=1000000, gamma=0.99, polyak=0.995, 
pi_lr=0.001, q_lr=0.001, batch_size=100, start_steps=10000, update_after=1000, update_every=50, 
act_noise=0.1, num_test_episodes=1, max_ep_len=1000, logger_kwargs={}, save_freq=1)