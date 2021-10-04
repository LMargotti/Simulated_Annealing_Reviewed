import unittest
import numpy as np
from numpy import random as rnd

from user_function import chosen_function
from algorithm import initialization, simulated_annealing
from core_functions import avg_last_k_value, boltz_acceptance_prob, boltz_move, geom_cooling, objective_limit, tolerance



class TestSA_alg(unittest.TestCase):
    """
    This file is intended to act as a test for the implemented algorithm and the core functions. 
    Tests are performed according to _unittest_ library documentation.
    
    A random seed is fixed for reproducibility.

    """
    
    def setUp(self):

        # Initialize unit test parameters
        TestSA_alg.initial_temp = 100
        TestSA_alg.interval = (-6, 6)
        TestSA_alg.alpha = 0.95
    
    
    
    def test_initialization(self):

        """
        Testing the initialization function: we impose conditions on T and s according to their definition
        """

        s, temp = initialization(self.initial_temp, self.interval)

        # Testing the temperature: input needs to be equal to the initial temperature the user sets.
        self.assertEqual(temp, self.initial_temp)

        # Testing the initial state: it must be confined in the given interval the algorithm operates into
        self.assertLessEqual(s[0], self.interval[1])
        self.assertLessEqual(s[1], self.interval[1])
        self.assertGreaterEqual(s[0], self.interval[0])
        self.assertGreaterEqual(s[1], self.interval[0])

    
    
    def test_move(self):  
        
        """
        Testing the Boltzmann move function
        """
        

        rnd.seed(42) #reproducibility

        s = (rnd.uniform(self.interval[0], self.interval[1]), rnd.uniform(self.interval[0], self.interval[1])) # initial state
        new_s = boltz_move(s, self.initial_temp, self.interval) 

        # The new state is in the given interval
        self.assertLessEqual(new_s[0], self.interval[1])
        self.assertLessEqual(new_s[1], self.interval[1])
        self.assertGreaterEqual(new_s[0], self.interval[0])
        self.assertGreaterEqual(new_s[1], self.interval[0])

    
    # Testing the validity of the implementation of energy:
    # we fix a random seed and compare the results of the generation with
    # a given function (2-D function: chosen_function)

    def test_energy(self):

        rnd.seed(42) #reproducibility

        """
        The values of energy for fixed seed need to be equal to the ones superimposed for a 2D function
        """
        

        s = (rnd.uniform(self.interval[0], self.interval[1]), rnd.uniform(self.interval[0], self.interval[1])) # initial state
        e = chosen_function(s)
        
        self.assertEqual(e, s[0]**2+s[1]**2)


    
    def test_cooling(self):
        
        """
        Testing the cooling method: for a given temperature, the application of cooling
        implies a _lower_ temperature. Moreover, geom_cooling works multiplying T by a constant: this needs also to be tested.
        """ 

        temp_0 = 100.
        temp_1 = geom_cooling(temp_0, self.alpha)

        self.assertLess(temp_1, temp_0) #Testing the definition of cooling

        self.assertEqual(temp_1, temp_0 * self.alpha) #Testing the correctness of the employed cooling

        self.assertGreater(temp_1,0) #Temperature must _always_ be positive

    

    def test_acceptance_prob(self):

        """
        Testing the acceptance probability function: it needs to output a value between 0 and 1. 
        Also, its definition implies that for two identical energies it returns 1.
        """ 

        rnd.seed(42) #reproducibility

        e1 = rnd.random()
        e2 = rnd.random()
        acc_prob = boltz_acceptance_prob(e1, e2, self.initial_temp)


        # Check if the returned value is comprised between 0 and 1
        self.assertLessEqual(acc_prob,1.)
        self.assertGreaterEqual(acc_prob,0.)

        # For equal energies the aceptance probability is 1
        e1 = rnd.random()
        e2 = e1
        acc_prob = boltz_acceptance_prob(e1, e2, self.initial_temp)

        self.assertEqual(acc_prob, 1.)

    
   

    def test_tolerance_criterion(self) :

        """
        Testing the tolerance criterion. Two scenarios are pictured depending on the definition of the tolerance iter.
        """

        energies = [1,2,3,4,5,6]
        flag1 = tolerance(energies, tolerance = 10, tolerance_iter = len(energies)+1)
        flag2 = tolerance(energies, tolerance = 10, tolerance_iter = len(energies)-1)
        
        self.assertFalse(flag1)
        self.assertTrue(flag2)

    
    

    def test_objective_limit(self) :

        """
        Testing the objective limit criterion: we set a limit for chosen_function that must not be overcome.
        """

        rnd.seed(42) #reproducibility

        s = (rnd.uniform(self.interval[0], self.interval[1]), rnd.uniform(self.interval[0], self.interval[1]))
        e =  chosen_function(s)
        flag = objective_limit(energy = e, limit = -1)
        
        self.assertFalse(flag)


    

    def test_sa(self) :

        """
        Test on ALGORITHM: test is run on chosen_function: the algorithm is correct if it gives a minimum in [0,0] for that specific function
        """

       
        
        states, energies, temp, k, _exit, reann = simulated_annealing(
                                                cooling = geom_cooling,
                                                energy = chosen_function,
                                                acceptance_prob = boltz_acceptance_prob,
                                                move = boltz_move,
                                                tolerance_value = 1e-10,
                                                initial_temp = self.initial_temp,
                                                interval = (-6, 6),
                                                verbose = True
                                                )
       # Check the minimum, rounding the obtained float to the lower integer (abs--->negative-to-positive conversion)
        delta_err = 1 
        print("Minimum:", states[-1])
        self.assertAlmostEqual(np.floor(abs(abs(states[-1][0])-delta_err)), 0.), "The found minimum is far from what expected"
        self.assertAlmostEqual(np.floor(abs(abs(states[-1][1])-delta_err)), 0.), "The found minimum is far from what expected"
        

    
   
    
if __name__ == '__main__':


    unittest.main()

