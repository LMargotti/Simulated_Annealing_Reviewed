"""
Algorithm implementation: a function is defined with default parameter and
everything is constructed inside it.
"""
import numpy as np
from numpy import random as rnd
from core_functions import tolerance, objective_limit

#this is the function with the interested parameters found in literature

def simulated_annealing(cooling, acceptance_prob, energy, move, interval, initial_temp = 100., 
                        k_max = 1e10, tolerance_value = 1e-6, tolerance_iter = 10,
                        obj_fn_limit = -1e10, reann_tol = 100, verbose = False):

     #Step 1: generation of random starting point.
    states = []
    energies = []
    temperatures = []
    s = (rnd.uniform(interval[0], interval[1]), rnd.uniform(interval[0], interval[1]))
    k = 0
    T = initial_temp
    reann = False
    exit_types = {
        0 : 'Max Iter',
        1 : 'Tolerance',
        2 : 'Obj Limit',
        3 : 'Temp Limit'
        }
    _exit = 0
    
    if verbose:
        dash = '-' * 70
        print("\n")
        print ('{:_^70}'.format('Simulated Annealing'))
        print("Test function", energy)
        print("Initial state: {}".format(s))
        print("\n")
    
    
    while True:
        #it generates <infinte> iterations to be stopped two lines below if certain
        #conditions are met.
        k += 1
        
        #Stopping criterion in case of max n.o. iterations is reached.
        if k == k_max :
            if verbose :
                print(dash)
                print("MAX ITERATION EXIT")
                print(dash)
            break           
        
