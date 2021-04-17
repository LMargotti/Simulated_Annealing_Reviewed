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
        
        #Step 2: move or generaton of new solution.
        new_s = move(s, T, interval)
        energy_s = energy(s)
        energy_new_s = energy(new_s)
        states.append(s)
        energies.append(energy_s)
        temperatures.append(T)
        
        #Step 3: application of Geometric cooling method.
        T = cooling(T)
        
        #Stopping criteria for algorithm interruption and results presentation.
        
        #Temperature limit 
        if T <= 0. :
            if verbose :
                print(dash)
                print("TEMPERATURE EXIT")
                print(dash)
            _exit = 3
            break   
        
       #Eneregy tolerance method, based on the average difference in energy
       #computed for N iterations.
        if tolerance(energies, tolerance_value, tolerance_iter) :
            if verbose :
                print(dash)
                print("TOLERANCE EXIT")
                print(dash)
            _exit = 1
            break    
        
        #minimum value of free energy is reached.
        if objective_limit(energy_s, obj_fn_limit) :
            if verbose :
                print(dash)
                print("OBJECTIVE FUNCTION LIMIT EXIT")
                print(dash)
            _exit = 2
            break
        
        #Reanniling Process if better solutions have been found along the way.
        best_e = min(energies)
        best_s = states[np.argmin(energies)]
        
        if energy_s > best_e + reann_tol :
            if verbose :
                print(dash)
                print("REANNILING")
                print(dash)
            energies = []
            states = []
            s = best_s
            energy_s = best_e
            T = initial_temp
            k = 0
            reann = True
            continue
        
        #Step 4: acceptance or rejection through comparison with acceptance probability.
        if acceptance_prob(energy_s, energy_new_s, T) >= rnd.random() :
            s = new_s
    
    return states, energies, temperatures, k, exit_types[_exit], reann
