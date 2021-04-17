
import matplotlib.pyplot as plt
import numpy as np
from test_functions import ackley_fn, himmelblau_fn, rastrigin_fn, rosenbrock_fn
from my_function import chosen_function

"""
The following functions are identical in parameters and working principle.
Separation is aimed to give easy access for the users to the chosen_function plot 
code lines if they want to change settings.
They generate specific points via for loop once a dedicated range is selected arbitrarily.
For test functions, actual local minima are black-labelled and reported in results plots: they 
show how far the algorithm is from exact solutions.
"""


def plot_results_myfunction(results):
    """
    Generation of selected 2-variables functions points.
    
    >Plot of specified function in a 3d graph via filling lists with the function values 
     evaluated at given points in a given range.
    >Plot of results applied to selected function with specified labels for local minima, starting point
     and iterative states.
    
    Pictures saved as .png format in a dedicated folder.
    
    Parameters
    ----------
    
    results: list
             This is actually a list of lists of the form
             results[function]=[[state],[energy],[temperature]] 
             where state=(x,y); energy is a function of (x,y) and temperature is the
             temperature at which the scalar of energy is evaluated.
    
    """
   #Generate chosen function points
    function={"chosen_function":[[],[],[]]}
    
    for i in range (-60, 60):
        for j in range (-60,60):
            function['chosen_function'][0].append(i/10)
            function['chosen_function'][1].append(j/10)
            function['chosen_function'][2].append(chosen_function((i/10, j/10)))

    fig = plt.figure( figsize = (20,10))
    
    #Chosen function is created as a single 3-dimensional plot. No operations performed yet.
    ax5 = fig.add_subplot(111, projection='3d', title = 'chosen_function')
    xs = function['chosen_function'][0]
    ys = function['chosen_function'][1]
    zs = function['chosen_function'][2]
    ax5.scatter(xs, ys, zs, marker='o')
    ax5.set_xlabel('x')
    ax5.set_ylabel('y')
    ax5.set_zlabel('energy')

    plt.savefig("./images/chosen_fuction.png")
    
    #Organize the results of performance test
    
    #Chosen function
    my_points = np.array(results['chosen_function'][0])
    my_energy = np.array(results['chosen_function'][1])
    my_temp = np.array(results['chosen_function'][2])
    
    #-----------results pics----------#

    fig = plt.figure( figsize = (20,10))
      
    #Result of the algorithm on Chosen function.  
    ax5 = fig.add_subplot(111, projection='3d', title = 'Chosen function test')
    xs = my_points[:,0]
    ys = my_points[:,1]
    zs = my_energy
    # Plot-options included for clarity i.e. starting point and actual data points.
    ax5.scatter(xs, ys, zs, marker='o', color = 'green', label = "data points")
    ax5.scatter(xs[0],ys[0],zs[0], color = 'red', marker = '*', s = 100, label = "initial point")
    #ax5.scatter([0.,0.,0.,0.], marker='^', s = 100, color = 'black', label = "global minima")
    ax5.legend()
    ax5.set_xlabel('x')
    ax5.set_ylabel('y')
    ax5.set_zlabel('energy')

    
    plt.savefig("./images/result.png")
    plt.show()


def plot_results_tests(results):
    """
    Generation of selected 2-variables functions points.
    
    >Plot of specified function in a 3d graph via filling lists with the function values 
     evaluated at given points in a given range.
    >Plot of results applied to selected function with specified labels for local minima, starting point
     and iterative states.
    
    Pictures saved as .png format in a dedicated folder.
    
    Parameters
    ----------
    results: list
             This is actually a list of lists of the form
             results[function]=[[state],[energy],[temperature]] 
             where state=(x,y); energy is a function of (x,y) and temperature is the
             temperature at which the scalar of energy is evaluated.
    
    """
    
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

    #---------Results plots------------#
    
    #Organize the results of the performance tests

    #Ackley
    ackley_points = np.array(results['Ackley'][0])
    ackley_energy = np.array(results['Ackley'][1])
    ackley_temp = np.array(results['Ackley'][2])

    #Himmelblau
    himm_points = np.array(results['Himmelblau'][0])
    himm_energy = np.array(results['Himmelblau'][1])
    himm_temp = np.array(results['Himmelblau'][2])

    #Rastrigin
    rastr_points = np.array(results['Rastrigin'][0])
    rastr_energy = np.array(results['Rastrigin'][1])
    rastr_temp = np.array(results['Rastrigin'][2])

    #Rosenbrock
    rosen_points = np.array(results['Rosenbrock'][0])
    rosen_energy = np.array(results['Rosenbrock'][1])
    rosen_temp = np.array(results['Rosenbrock'][2])


    # Plots
    # Local minima can be found in literature; they demonstrate the consistency of the algorithm. 
    fig = plt.figure( figsize = (20,10))
 
    #Ackley plot
    ax1 = fig.add_subplot(221, projection='3d', title = 'Ackley test')
    xs = ackley_points[:,0]
    ys = ackley_points[:,1]
    zs = ackley_energy
    ax1.scatter(xs, ys, zs, marker='o', color = 'green', label = "data points")
    ax1.scatter(xs[0],ys[0],zs[0], color = 'red', marker = '*', s = 100, label = "initial point")
    ax1.scatter(0.,0.,0., marker='^', s = 100, color = 'black', label = "global minimum")
    ax1.legend()
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')
    ax1.set_zlabel('energy')

    #Himmelblau plot
    ax2 = fig.add_subplot(222, projection='3d', title = 'Himmelblau test')
    xs = himm_points[:,0]
    ys = himm_points[:,1]
    zs = himm_energy
    ax2.scatter(xs, ys, zs, marker='o', color = 'green', label = "data points")
    ax2.scatter(xs[0],ys[0],zs[0], color = 'red', marker = '*', s = 100, label = "initial point")
    ax2.scatter([3,-2.805118, -3.779310, 3.584428], [2, 3.131312,-3.283186,-1.848126],[0.,0.,0.,0.], 
                marker='^', s = 100, color = 'black', label = "global minima")
    ax2.legend()
    ax2.set_xlabel('x')
    ax2.set_ylabel('y')
    ax2.set_zlabel('energy')

    #Rastrigin plot
    ax3 = fig.add_subplot(223, projection='3d', title = 'Rastrigin test')
    xs = rastr_points[:,0]
    ys = rastr_points[:,1]
    zs = rastr_energy
    ax3.scatter(xs, ys, zs, marker='o', color = 'green', label = "data points")
    ax3.scatter(xs[0],ys[0],zs[0], color = 'red', marker = '*', s = 100, label = "initial point")
    ax3.scatter(0.,0.,0., marker='^', s = 100, color = 'black', label = "global minimum")
    ax3.legend()
    ax3.set_xlabel('x')
    ax3.set_ylabel('y')
    ax3.set_zlabel('energy')

    #Rosenbrock plot
    ax4 = fig.add_subplot(224, projection='3d', title = 'Rosenbrock test')
    xs = rosen_points[:,0]
    ys = rosen_points[:,1]
    zs = rosen_energy
    ax4.scatter(xs, ys, zs, marker='o', color = 'green', label = "data points")
    ax4.scatter(xs[0],ys[0],zs[0], color = 'red',marker = '*', s = 100, label = "initial point")
    ax4.scatter(1.,1.,0., marker='^', s = 100, color = 'black', label = "global minimum")
    ax4.legend()
    ax4.set_xlabel('x')
    ax4.set_ylabel('y')
    ax4.set_zlabel('energy')

    plt.savefig("./images/results.png")
    plt.show()

