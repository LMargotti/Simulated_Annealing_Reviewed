import unittest
import numpy as np
from numpy import random as rnd

from core_functions import avg_last_k_value, boltz_acceptance_prob, boltz_move, geom_cooling, objective_limit, tolerance

"""
This file is intended to act as a test for the implemented algorithm and the core functions. 
Tests are performed according to _unittest_ library documentation.

The following introduces a check on the proposed functions via analysis of an arbitrarily chosen well known 2-D function,
in order for its behaviour to be easily controlled from scratch. 

Energy function the tests are performed on: f(x)=x^2+y^2.
"""
class TestSA_alg(unittest.TestCase):
    def energy(self, x):

        # Checking for input dimensionality: the system ensures the input is a 2-D function
        self.assertEqual(len(x), 2) 

        return x[0]**2+x[1]**2
    
    def tolerance(self, energies, tolerance, tolerance_iter) :
        """
        The algorithm runs until the average change in value of the objective function 
        is less than the tolerance.
        """
        
        if len(energies) <= tolerance_iter :
            return False

        avg_last_k = avg_last_k_value(energies, tolerance_iter)

        # Tests on the avg: we need the average of the last values of energies list to be greater than 0, otherwise 
        # errors occurred in the evaluation of the mean

        # Print(energies) to be added if needed
        self.assertGreaterEqual(avg_last_k, 0)

        if avg_last_k < tolerance :
            return True
        else : 
            return False
    
    # ALGORITHM

    def simulated_annealing(self, cooling, acceptance_prob, move, interval, initial_temp = 100., 
                        k_max = 1e10, tolerance_value = 1e-6, tolerance_iter = 10,
                        obj_fn_limit = -1e10, reann_tol = 100, verbose = False):

        """
        [see algorithm.py]

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


        # Input values check: ensures the user does not type undesired values.
        self.assertGreater(initial_temp,0), "Initial temperature needs to be a positive float"
        self.assertGreater(reann_tol, 0), "Insert positive values"
        self.assertGreater(tolerance_iter, 0), "Insert positive values"
        self.assertGreater(k_max, 0), "Insert positive values"
        
        # Step 1: generation of random starting point.
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
            print("Initial state: {}".format(s))
            print("\n")
        
        
        while True:
            # It generates <infinte> iterations to be stopped two lines below if certain
            # conditions are met.
            k += 1
            
            # Stopping criterion in case of max n.o. iterations is reached.
            if k == k_max :
                if verbose :
                    print(dash)
                    print("MAX ITERATION EXIT")
                    print(dash)
                break    


            # Step 2: move or generaton of new solution.
            new_s = move(s, T, interval)

            # Testing on the validity of the proposed solution and the clip method: it needs to lay in the selected interval.
            self.assertLessEqual(new_s[0], interval[1])
            self.assertLessEqual(new_s[1], interval[1])
            self.assertGreaterEqual(new_s[0], interval[0])
            self.assertGreaterEqual(new_s[1], interval[0])

            energy_s = self.energy(s)
            energy_new_s = self.energy(new_s)

            # Check if the energy function returned value for s and new_s is consistent with our paraboloid 
            self.assertEqual(energy_s, s[0]**2+s[1]**2)
            self.assertEqual(energy_new_s, new_s[0]**2+new_s[1]**2)

            states.append(s)
            energies.append(energy_s)
            temperatures.append(T)
            
            # Step 3: application of Geometric cooling method.
            T = cooling(T)
            
            # Stopping criteria for algorithm interruption and results presentation.
            
            # Temperature limit 
            if T <= 0. :
                if verbose :
                    print(dash)
                    print("TEMPERATURE EXIT")
                    print(dash)
                _exit = 3
                break   
            
           # Enregy tolerance method, based on the average difference in energy
           # computed for N iterations.
            elif self.tolerance(energies, tolerance_value, tolerance_iter) :
                if verbose :
                    print(dash)
                    print("TOLERANCE EXIT")
                    print(dash)
                _exit = 1
                break    
            
            # Minimum value of free energy is reached.
            elif objective_limit(energy_s, obj_fn_limit) :
                if verbose :
                    print(dash)
                    print("OBJECTIVE FUNCTION LIMIT EXIT")
                    print(dash)
                _exit = 2
                break
            
            # Reanniling Process if better solutions have been found along the way.
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
            
            # Step 4: acceptance or rejection through comparison with acceptance probability.
            acc_prob = acceptance_prob(energy_s, energy_new_s, T)


            # Check if the returned value is comprised between 0+ and 1
            self.assertLessEqual(acc_prob,1.)
            self.assertGreater(acc_prob,0.)

            if acc_prob >= rnd.random() :
                s = new_s
        
        return states, energies, temperatures, k, exit_types[_exit], reann       




    def test_minimum(self):
        states, energies, temp, k, _exit, reann = self.simulated_annealing(
                                                cooling = geom_cooling,
                                                acceptance_prob = boltz_acceptance_prob,
                                                move = boltz_move,
                                                tolerance_value = 1e-10,
                                                initial_temp = 100,
                                                interval = (-6, 6),
                                                verbose = True
                                                )
    # Check the minimum, rounding the obtained float to the lower integer (abs--->negative-to-positive conversion)
        delta_err = 1 #arbitrarily chosen error 
        print("Minimum:", states[-1])
        self.assertAlmostEqual(np.floor(abs(abs(states[-1][0])-delta_err)), 0.), "The found minimum is far from what expected"
        self.assertAlmostEqual(np.floor(abs(abs(states[-1][1])-delta_err)), 0.), "The found minimum is far from what expected"
        

if __name__ == '__main__':

    unittest.main()

