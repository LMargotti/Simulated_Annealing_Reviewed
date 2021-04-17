#------------------------------------------------------#
#------------Simulated Anneanling algorithm------------#
#------------------------------------------------------#
import numpy as np
from numpy import random as rnd
from core_functions import tolerance, objective_limit

#this is the function with the interested parameters found in literature

def simulated_annealing(cooling, acceptance_prob, energy, move, interval, initial_temp = 100., 
                        k_max = 1e10, tolerance_value = 1e-6, tolerance_iter = 10,
                        obj_fn_limit = -1e10, reann_tol = 100, verbose = False):

"""
    The algorithm is aimed to iterate a specific procedure in order
    to reach global minima of given functions.
    
    It generates an initial random point s=s_0 with initial
    temperature T=t_0; a new candidate is then proposed and is checked
    whether if it's acceptable or not through delta_e and related 
    probability.
    
    With cooling methods (in that specific case: Geometric cooling 
    algorithm), temperature is decreased: the move length is changed
    accordingly.
    
    Re-annealing process is then performed whenever a non-optimal solution
    is reached (if s*(k+n) is worse than s*(k+b), n and b being random indexes):
    this avoids the algorithm being trapped into local minima.
    
    Program interrupts if specific conditions are achieved (e.g. max. number of 
                                                            iterations met,
                                                            T-->0,
                                                            Energy is at its minimum,
                                                            Energy tolerance is overcome).
    
    Parameters
    ----------
    cooling: function
             It makes temperature lowering possible while running the algorithm.
        
    acceptance_prob: float
                     Number in the ]0,1] interval, representing the probability to be used
                     for data acceptance or rejection.
        
    energy: float
            Specific Gibbs free energy
        
    move: function
          It applies the definition of boltz_move for generating new candidates.
        
    interval: list-like
              Estremes of a given interval.
    
    initial_temp: float
                  Parameter to be set from output [else: default initial temperature]
        
    k_max: int
           Parameter to be set from output [else: default Max number of iterations]
           
    tolerance_value: float
                     Parameter to be set from output [else: default tolerance Energy value for stopping criterion]
                     
    tolerance_iter: int
                    Parameter to be set from output [else: default number of iterations taken into account in Tolerance Energy]
        
    obj_fn_limit: float
                  Parameter to be set from output [else: default objective function limit]
        
    reann_tol: float
               Parameter to be set from output [else: default reanniling tolerance value]
               
    [verbose: bool
              It makes the system print out further details of iteration procedures.]
    
    """

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
