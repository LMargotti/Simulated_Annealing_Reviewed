import unittest
import numpy as np
from numpy import random as rnd

from core_functions import avg_last_k_value, boltz_acceptance_prob, boltz_move, geom_cooling, objective_limit, tolerance

"""

Unit test correction: you need a complete test to be operated on the whole algorithm
that allows the user not to be lost while finding errors or bugs.

Idea: I'll create a class (?) and implement testing methods in order for my core functions
and algorithm to be controlled from scratch with a simple mathematical 2-D function (a paraboloid?).

"""
class TestSA_alg(unittest.TestCase):
    def energy(self, x):

        self.assertEqual(len(x), 2) # Checking for input dimensionality

        return x[0]**2+x[1]**2
    
    def tolerance(self, energies, tolerance, tolerance_iter) :
        """
        The algorithm runs until the average change in value of the objective function 
        is less than the tolerance.
        """
        
        if len(energies) <= tolerance_iter :
            return False

        avg_last_k = avg_last_k_value(energies, tolerance_iter)

        #tests on the avg(?) not working, need further work
        #print(energies)
        #self.assertLessEqual(avg_last_k, max(energies))
        #self.assertGreaterEqual(avg_last_k, min(energies))

        if avg_last_k < tolerance :
            return True
        else : 
            return False
    
    #ALGORITHM

    def simulated_annealing(self, cooling, acceptance_prob, move, interval, initial_temp = 100., 
                        k_max = 1e10, tolerance_value = 1e-6, tolerance_iter = 10,
                        obj_fn_limit = -1e10, reann_tol = 100, verbose = False):

        """
        
        Parameters
        ----------
        cooling: function
                 It makes temperature lowering possible while running the algorithm.
            
        acceptance_prob: float
                         Number in the ]0,1] interval, representing the probability to be used
                         for data acceptance or rejection.
            
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


        # Input values check
        self.assertGreater(initial_temp,0), "Initial temperature needs to be a positive float"
        self.assertGreater(reann_tol, 0), "Insert positive values"
        self.assertGreater(tolerance_iter, 0), "Insert positive values"
        self.assertGreater(k_max, 0), "Insert positive values"


"""
Notes while coding:

I'll need to import libraries and files. 
>I'll have a new(!!!) function here, so no need for the algorithm to be imported
>core functions needed tho

Write functions to be tested. For example, define an energy of the form 
x^2+y^2 and test whether if the given array is of dimension = 2

I can test also the correctness of the minimum, the validity of the expected "move" i.e. (prob in [0,1])
and the input values consistency (i.e. T>0)
"""