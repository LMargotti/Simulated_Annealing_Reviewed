#insert user function
#import numpy as np
INTERVAL=[-6,6]
def chosen_function(X):
    """
    It creates chosen_function of X = (x,y).
    
    User function is computed following usual mathematical approaches, remember
    to include dedicated libraries if needed and to set different interval eventually if needed.
 
    Requirements for readability: real, 2-variable non pathological function.
    
    
    """
    x=X[0]
    y=X[1]
    
    #Insert your function of interest here, remember to change INTERVAL values if needed.#
    #for example
    a=x**2+y**2

    #test function for correctness of implemented value.
    if type(a) == float:
        
        return(a)
    else:
        assert type(a) == np.float64
        return(a)
    #pass