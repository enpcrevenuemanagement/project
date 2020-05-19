import tensorflow
from gym_env import *
import spinup


# Vols proposés
V1 = Vol((10,30),5)
V2 = Vol((18,30),5)
flights = [V1,V2]


# Nombre de clients dans la file (longueur d'un épisode)
N = 10

# On construit l'environnement Gym
env_fn = RMenv(flights, N)

#On donne la fonction actor-critic : argument facultatif ?
fn_mlp_actor_critic = None

# On run l'algo
spinup.ddpg_tf1(env_fn, actor_critic=fn_mlp_actor_critic, ac_kwargs={}, 
seed=0, steps_per_epoch=4000, epochs=100, replay_size=1000000, gamma=0.99, polyak=0.995, 
pi_lr=0.001, q_lr=0.001, batch_size=100, start_steps=10000, update_after=1000, update_every=50, 
act_noise=0.1, num_test_episodes=10, max_ep_len=1000, logger_kwargs={}, save_freq=1)