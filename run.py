import argparse
import algorithm as ag
from core_functions import boltz_acceptance_prob, boltz_move, geom_cooling
from my_function import chosen_function, INTERVAL
from plot import plot_results_myfunction, plot_results_tests
from test_functions import ackley_fn,  himmelblau_fn, rastrigin_fn, rosenbrock_fn


if __name__ == '__main__':

    """
    Command-line parsing for parameters management.
    Full alphabetic-ordered list of available options in Readme.md
    Every parser is dedicated to a specific variable to be modified.
    
    """
    
    parser = argparse.ArgumentParser(description='Simulated Annealing Algorithm', formatter_class=argparse.RawTextHelpFormatter)
    
    parser.add_argument('-k', '--k_max', action='store', nargs='?', const=None, default=1e6, type=int,
                        choices=None, help='Max number of iterations. [default: 1e6]', metavar=None)
    
    parser.add_argument('-m', '--mode', action='store', nargs='?', const=None, default='test', type=str,
                        choices=None, help='[default: "test"]', metavar=None)
    
    parser.add_argument('-o', '--obj_fn_limit', action='store', nargs='?', const=None, default=-1e10, type=float,
                        choices=None, help='Objective function limit. [default: -1e10]', metavar=None)
    
    parser.add_argument('-r', '--reann', action='store', nargs='?', const=None, default=100, type=float,
                        choices=None, help='Reanniling tolerance value.[default: 100]', metavar=None)
    
    parser.add_argument('-t', '--init_temp', action='store', nargs='?', const=None, default=100, type=float,
                        choices=None, help='Initial temperature. [default: 100]', metavar=None)
    
    parser.add_argument('-ti', '--tolerance_iter', action='store', nargs='?', const=None, default=1000, type=int,
                        choices=None, help='Number of iterations taken into account in Tolerance Energy. [default: 1000]', metavar=None)
    
    parser.add_argument('-tv', '--tolerance_value', action='store', nargs='?', const=None, default=1e-10, type=float,
                        choices=None, help='Tolerance Energy value for stopping criterion [default: 1e-6]', metavar=None)
            
    parser.add_argument('-v', '--verbose', action='store', nargs='?', const=None, default=False, type=bool,
                        choices=None, help='[default: False]', metavar=None)
        
    args = parser.parse_args()
    
    """
    Test functions for input correctness
    """
    assert args.init_temp > 0, "Initial temperature needs to be a positive float"
    assert args.reann > 0, "Insert positive values"
    assert args.tolerance_iter > 0, "Insert positive values"
    assert args.k_max > 0, "Insert positive values"

# Configuration mode: test functions are used for no "-m" command request.

    if args.mode == 'test':

        test_conf = {
            "Ackley" : [ackley_fn, (-6, 6) ],
            "Himmelblau" : [himmelblau_fn, (-6, 6)],
            "Rastrigin" : [rastrigin_fn, (-5.12, 5.12)],
            "Rosenbrock" : [rosenbrock_fn, (-6, 6)]
        }
        results = {
            "Ackley" : [],
            "Himmelblau" : [],
            "Rastrigin" : [],
            "Rosenbrock" : []
        }
        exit_interations = {
            "Ackley" : [],
            "Himmelblau" : [],
            "Rastrigin" : [],
            "Rosenbrock" : []
        } 

    elif args.mode == "userf":
        test_conf = {
            "chosen_function" : [chosen_function, INTERVAL]
        }
        results = {"chosen_function" : []
            }
        exit_interations = {
            "chosen_function" : []
            }

    """
    The algorithm is run according to configuration setup.
    For cycle is dedicated to test functions only in order to
    process them and have them plotted in the same 
    image.

    """

    for fn, par in test_conf.items():
        states, energies, temp, k, _exit, reann = ag.simulated_annealing(
                                                        cooling = geom_cooling,
                                                        acceptance_prob = boltz_acceptance_prob,
                                                        energy = par[0],
                                                        move = boltz_move,
                                                        interval = par[1],
                                                        initial_temp = args.init_temp,
                                                        k_max = args.k_max,
                                                        tolerance_value = args.tolerance_value,
                                                        tolerance_iter = args.tolerance_iter,
                                                        obj_fn_limit = args.obj_fn_limit,
                                                        reann_tol = args.reann,
                                                        verbose = args.verbose
                                                        )
        
        
        #creating specific lists to be fulfilled with obtained values
        results[fn].append(states)
        results[fn].append(energies)
        results[fn].append(temp)
        exit_interations[fn].append(_exit)
        exit_interations[fn].append(k)
        exit_interations[fn].append(reann)
    
    
    # Results: output shows specific function, stopping criterion, number of iterations and if reannealing occurred + last point to be tested
    for k,v in exit_interations.items():
        print("\n")
        print("Function: {}\nStopping criterion: {}\nNumber of iterations: {}\nReanniling: {}".format(k,v[0],v[1], v[2]))

    # Plots
    if args.mode == 'test':
        plot_results_tests(results)
        
    else:
        plot_results_myfunction(results)
