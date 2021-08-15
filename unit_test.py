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

        #how can I test it?

#Algorithm here



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