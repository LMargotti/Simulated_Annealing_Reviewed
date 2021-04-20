import unittest
import numpy as np

import algorithm as ag
from core_functions import boltz_acceptance_prob, boltz_move, geom_cooling
from plot import plot_results_myfunction, plot_results_tests
from test_functions import ackley_fn,  himmelblau_fn, rastrigin_fn, rosenbrock_fn


class TestSA_alg(unittest.TestCase):

    def test_minimum(self):
        states, energies, temp, k, _exit, reann = ag.simulated_annealing(
                                                cooling = geom_cooling,
                                                acceptance_prob = boltz_acceptance_prob,
                                                energy = ackley_fn,
                                                move = boltz_move,
                                                tolerance_value = 1e-10,
                                                initial_temp = 100,
                                                interval = (-6, 6)
                                                )
        # Found minimum
        x = np.abs(round(states[-1][0],2))
        y = np.abs(round(states[-1][1],2)) 
        # True minimum
        x0 = 0. 
        y0 = 0.
        # Delta
        delta = 1.2

        # 
        cond1 = (x0 <= x + delta) and (x0 >= x - delta)
        cond2 = (y0 <= y + delta) and (y0 >= y - delta)

        print(x, y)

        self.assertTrue(cond1)
        self.assertTrue(cond2)


if __name__ == '__main__':
    unittest.main()