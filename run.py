import algorithm as ag
from core_functions import geom_cooling, boltz_acceptance_prob, boltz_move
from test_functions import ackley_fn, rastrigin_fn, rosenbrock_fn, himmelblau_fn

if __name__ == '__main__':
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
    else break
    
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
    
    
    # Results: output shows specific function, stopping criterion, number of iterations and if reannealing occurred.
    for k,v in exit_interations.items():
        print("\n")
        print("Function: {}\nStopping criterion: {}\nNumber of iterations: {}\nReanniling: {}".format(k,v[0],v[1], v[2]))