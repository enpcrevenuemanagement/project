import tensorflow as tf
import spinup

import wandb

#Importer les autre scripts
from gym_env import *
from vol import *

# horizon temporel (longueur d'un épisode = nombre de clients si demande equirepartie)
T = 9

# Initialisation des vols

h1 = Horaire(14,0)
V1 = Vol(h1,T+1)

h2 = Horaire(19,0)
V2 = Vol(h2,10)

flights = [V1]
# Range d'exploration du prix
max_price = 200

name = "ddpg_" + str(T) + "_V1"

# On construit l'environnement Gym
env = RMenv(flights, T, max_price, verbose = 0)
# On donne le constructeur de l'environnement Gym
env_fn = lambda : env

# If the environment don't follow the interface, an error will be thrown
from stable_baselines.common.env_checker import check_env
check_env(env, warn=True)

hp = dict(

    #env params
    max_price = max_price,
    time_horizon = T,

    # epochs
    epochs=100,
    # steps = interactions = clients
    steps_per_epoch=4000,
    # Number of new env interactions btw each new grad descent
    update_every=100, 

    #Uniform start steps
    start_steps=8000, 
    # Min env interactions before first grad descent
    update_after=1000,

    # Size of replay buffer
    replay_size=100000, 
    # Batch size from buffer for grad descent
    batch_size=1000, 


    #Learning rates
    pi_lr = 0.001, 
    q_lr = 0.001, 
    # Bruit gaussien random de std dev = act_noise
    act_noise=0.5,
    # Discount = 1 for finite horizon
    gamma=0.99, 
    # "Lag" of the target network
    polyak=0.1, 

    # Num test episodes ??
    num_test_episodes=1000,

    # Episode length (si done == false tout le temps)
    # en pratique doit etre supérieur à min(total seats, total clients)
    max_ep_len=1000, 

    logger_kwargs={}, 
    save_freq=1
    #actor_critic=<function mlp_actor_critic>
    #ac_kwargs={}, 
    #seed=0

    )



wandb.init(project=name, sync_tensorboard=True,config=hp)
config = wandb.config


# On run l'algo
spinup.ddpg_tf1(env_fn, 

epochs = config.epochs,
steps_per_epoch = config.steps_per_epoch,
start_steps = config.start_steps, 
update_after = config.update_after,
update_every = config.update_every, 
replay_size = config.replay_size, 
batch_size = config.batch_size, 
pi_lr = config.pi_lr, 
q_lr = config.q_lr, 
act_noise = config.act_noise,
gamma = config.gamma, 
polyak = config.polyak, 
num_test_episodes = config.num_test_episodes,
max_ep_len = config.max_ep_len, 
#logger_kwargs={}, 
#save_freq=1
#actor_critic=<function mlp_actor_critic>
#ac_kwargs={}, 
#seed=0

)