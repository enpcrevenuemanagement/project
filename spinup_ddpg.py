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

flights = [V1]

# horizon temporel (longueur d'un épisode = nombre de clients si demande equirepartie)
T = 10

# Range d'exploration du prix
max_price = 200

# On construit l'environnement Gym
env = RMenv(flights, T, max_price, verbose = 0)
# On donne le constructeur de l'environnement Gym
env_fn = lambda : env

# If the environment don't follow the interface, an error will be thrown
from stable_baselines.common.env_checker import check_env
check_env(env, warn=True)

# On run l'algo
spinup.ddpg_tf1(env_fn, 
#actor_critic=<function mlp_actor_critic>
#ac_kwargs={}, 
#seed=0,

steps_per_epoch=4000, 

# epochs
epochs=100, 

replay_size=1000000, 

#Discount
gamma=0.99, 


polyak=0.995, 

#Learning rates
pi_lr=0.01, 
q_lr=0.01, 

# Number of episodes par epoch ??
batch_size=100, 

#Uniform start steps
start_steps=10000, 
update_after=1000, 
update_every=50, 
# Bruit gaussien random de std dev = act_noise
act_noise=1, 

# Num test episodes ??
num_test_episodes=1,

# Episode length (si done == false tout le temps)
# en pratique doit etre supérieur à min(total seats, total clients)
max_ep_len=1000, 

logger_kwargs={}, 
save_freq=1)