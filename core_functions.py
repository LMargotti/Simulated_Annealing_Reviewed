#write the functions to be used for algorithm implementation

import numpy as np
from numpy import random as rnd

#move definition + clipping in order not to overcome domain limits

def boltz_move(state, temp, interval):
    new_state = [0,0]
    n = rnd.random()
    if n < 0.5 :
        new_state[0] = state[0] + np.sqrt(temp)
        new_state[1] = state[1] + np.sqrt(temp)
        return (clip(new_state[0], interval, state[0]), 
                clip(new_state[1], interval, state[1]))
    else :
        new_state[0] = state[0] - np.sqrt(temp)
        new_state[1] = state[1] - np.sqrt(temp)
        return (clip(new_state[0], interval, state[0]), 
                clip(new_state[1], interval, state[1]))


def clip(x, interval, state):
    a,b = interval   
    if x < a :
        return rnd.uniform(a, state)    
    if x > b :
        return rnd.uniform(state, b)    
    else: 
        return x

#boltzmann acceptance probability + cooling 

def boltz_acceptance_prob(energy, new_energy, temperature):
    delta_e = new_energy - energy   
    if delta_e < 0 :
        return 1
    else:
        return np.exp(- delta_e / temperature)


def boltz_cooling(initial_temp, k):
    #Boltzmann temperature decreasing.
    if k <= 1:
        return initial_temp
    else:
        return initial_temp / np.log(k)

def geom_cooling(temp, alpha = 0.95):
    #geometric cooling, T(k+1)=alpha*T(k)
    return temp * alpha


