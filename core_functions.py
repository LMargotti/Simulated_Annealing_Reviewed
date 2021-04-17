"""
Operative functions to be run into the SA_algorithm.
Creation of initial value, definition of 2-D movements and dedicated 
domain boundaries conditions, optimization methods and stopping criteria 
are listed below.
"""

import numpy as np
from numpy import random as rnd

#-------Neighbour generation----------#


def boltz_move(state, temp, interval):
    
    """
    The concept of "move" is here presented: the function defines the steps, whose
    magnitude and directions are expressed as the square root of <<current>> temperature
    and through random values of an uniform distribution respectively.
    
    Parameters
    ----------
    
    new_state: list
               It labels x and y axes.
               
    n: float
       Random index for move direction choice: positive for n<0.5, negative otherwise.
       
    Returns
    ----------  
    new_state: list
               The actual position is updated to the new state after addition/subtraction operations. 
               The new state is inside the function domain (see <<clip>>).
    
    """
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
    """
    <<Clip>> function allows for confinement of the moves inside the domain.   
    If x is not in interval, 
    return a point chosen uniformly at random between the violated boundary
    and the previous state; otherwise return x.
    
    Parameters
    ----------
    
    x: float
       Number to be clipped.
       
    interval: list-like
              Estremes of a given interval.
              
    state: float
           Current position
              
    """
    a,b = interval   
    if x < a :
        return rnd.uniform(a, state)    
    if x > b :
        return rnd.uniform(state, b)    
    else: 
        return x

#-----------Acceptance function--------------#

def boltz_acceptance_prob(energy, new_energy, temperature):
    """
    Boltzmann Annealing: the function generates a probability value to be considered
    when deciding whether if it's convenient or not for the transition to occur.
    It returns a float in the ]0,1] interval.
    
    Parameters
    ----------
    
    energy: float
            Gibbs free energy of the current state at given temperature.
            
    new_energy: float
                Gibbs free energy of the hypothetic next state at given temperature.
                
    temperature: float
                 Self-explained variable to be fixed and/or changed via parsing in order to modify the
                 jump length.
    """
    delta_e = new_energy - energy   
    if delta_e < 0 :
        return 1
    else:
        return np.exp(- delta_e / temperature)


#-----------Cooling Procedure---------------#
#Other cooling methods exist and can be found in references [1], [2]

def geom_cooling(temp, alpha = 0.95):
    """
    Geometric temperature decreasing procedure allows for temperature variations 
    after every iteration (k).
    It returns a value of temperature such that 
    T(k+1)=alpha*(T)
    
    Parameters
    ----------
    temp: float
          Current temperature.
    
    alpha: float
           Fixed geometric ratio.
    """
    return temp * alpha


#-----------Stopping Conditions------------#


def tolerance(energies, tolerance, tolerance_iter) :
    """
    The algorithm runs until the average change in value of the objective function 
    is less than the tolerance.
    """
    
    if len(energies) <= tolerance_iter :
        return False
    if avg_last_k_value(energies, tolerance_iter) < tolerance :
        return True
    else : 
        return False
    

def objective_limit(energy, limit):
    """
    The algorithm stops as soon as the current objective function value
    is less or equal then limit.
    """
    if energy <= limit :
        return True
    else :
        return False


def avg_last_k_value(energies, k):
    """
    Compute the average of the last k absolute differences between the values of a list.
    """
    diff = []
    L = len(energies)    
    for i in range(L - 1,L - (k+1),-1):
        diff.append(abs(energies[i]-energies[i-1]))
    return np.mean(diff)
