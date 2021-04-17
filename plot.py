#with matplotlib, plot the functions and the results

import matplotlib.pyplot as plt
import numpy as np
from test_functions import ackley_fn, himmelblau_fn, rastrigin_fn, rosenbrock_fn
from my_function import chosen_function

def plot_results_tests(results):
     #--------Test functions plots---------#

    #Generate functions points
    functions = {
                "Ackley" : [[],[],[]],
                "Himmelblau" : [[],[],[]],
                "Rastrigin" : [[],[],[]],
                "Rosenbrock" : [[],[],[]]               
                }

    for i in range(-60, 60):
        for j in range(-60, 60):
            functions['Ackley'][0].append(i/10)
            functions['Ackley'][1].append(j/10)
            functions['Ackley'][2].append(ackley_fn((i/10, j/10)))
            
            functions['Himmelblau'][0].append(i/10)
            functions['Himmelblau'][1].append(j/10)
            functions['Himmelblau'][2].append(himmelblau_fn((i/10, j/10)))
                    
            functions['Rosenbrock'][0].append(i/10)
            functions['Rosenbrock'][1].append(j/10)
            functions['Rosenbrock'][2].append(rosenbrock_fn((i/10, j/10)))
            
            

    for i in range(-512, 512, 10):
        for j in range(-512, 512, 10):
                    
            functions['Rastrigin'][0].append(i/100)
            functions['Rastrigin'][1].append(j/100)
            functions['Rastrigin'][2].append(rastrigin_fn((i/100, j/100)))

    fig = plt.figure( figsize = (20,10))

    #Ackley function
    ax1 = fig.add_subplot(221, projection='3d', title = 'Ackley')
    xs = functions['Ackley'][0]
    ys = functions['Ackley'][1]
    zs = functions['Ackley'][2]
    ax1.scatter(xs, ys, zs, marker='o')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('energy')

    #Himmelblau function
    ax2 = fig.add_subplot(222, projection='3d', title = 'Himmelblau')
    xs = functions['Himmelblau'][0]
    ys = functions['Himmelblau'][1]
    zs = functions['Himmelblau'][2]
    ax2.scatter(xs, ys, zs, marker='o')
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('energy')

    #Rastrigin function
    ax3 = fig.add_subplot(223, projection='3d', title = 'Rastrigin')
    xs = functions['Rastrigin'][0]
    ys = functions['Rastrigin'][1]
    zs = functions['Rastrigin'][2]
    ax3.scatter(xs, ys, zs, marker='o')
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_zlabel('energy')

    #Rosenbrock function
    ax4 = fig.add_subplot(224, projection='3d', title = 'Rosenbrock')
    xs = functions['Rosenbrock'][0]
    ys = functions['Rosenbrock'][1]
    zs = functions['Rosenbrock'][2]
    ax4.scatter(xs, ys, zs, marker='o')
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('energy')
    

    plt.savefig("./images/test_fn.png")

