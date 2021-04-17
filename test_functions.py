  
"""
Mathematical definition of the selected 2-variable test functions.
The reason behind this exact choice is found in the nature of 
the functions being full of peaks and singularities (Ackley, Rastrigin) or
with very low moduli of partial derivatives values(Himmelblau, Rosenbrock).
Dedicated links in Readme.md
"""

import numpy as np
from numpy import random as rnd


#------------Ackley function---------- 

def ackley_fn (X):
    """ 
    Returns the Ackley function of X=(x,y)
    """
    x = X[0]
    y = X[1]
    exp1 = np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))
    exp2 = np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y)))      
    return -20 * exp1 - exp2 + np.e + 20



#----------Himmelblau function---------   

def himmelblau_fn (X):
    """
    Returns the Himmelblau function of X=(x,y)
    """
    x = X[0]
    y = X[1]
    return np.square(x**2 + y - 11) + np.square(x + y**2 - 7)

    

#----------Rastrigin function----------  

def rastrigin_fn (X):
    """
    Returns the Rastrigin function of X=(x,y)
    """
    x = X[0]
    y = X[1]
    return 20 + x**2 + y**2 - 10 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))



#---------Rosenbrock function----------

def rosenbrock_fn (X):
    """
    Returns the Rosenbrock function of X=(x,y)
    """
    x = X[0]
    y = X[1]
    return np.square(1 - x) + 100 * np.square(y - x**2)