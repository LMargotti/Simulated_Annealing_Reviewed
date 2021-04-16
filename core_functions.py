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

