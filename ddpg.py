import numpy as np

#ALGO DE DDPG

def ddpg(theta, phi, D):
    #theta = initial policy parameters
    #phi = Q function parameters 
    #D = empty replay buffer
    
    #initialize
    theta_targ = theta
    phi_targ = phi

    for episodes: 
        #observe state s
        a = clip(mu_theta(s)+eps,alow,ahigh) #find action to execute
        #execute action a 
        #observe reward r, next state s_next and signal d (wether s_next is terminal)
        #store (s,a,r,s_next,d) in replay Buffer D
        if s_next is terminal:
            #reset environment state
        if time to update:
            for however many updates to do:
                #prendre un batch au hasard dans D : (s,a,r,s_next,d)
                #compute target :
                y(r,s_next,d) = r + gamma(1-d)*Q_phi_targ(s_next, mu_theta_targ(s_next))
                #update Q fonction by one step of gradient descent
                Q = Q - learning_rate*grad(Q) 
                #update policy by one step of gradient ascent
                mu = mu + learning_rate*grad(mu) 
                #update target network 
                phi_targ = rho*phi_targ + (1-rho)*phi
                theta_targ = rho*theta_targ + (1-rho)*theta

            end for 
        end if
    end for  #fin des épisodes






