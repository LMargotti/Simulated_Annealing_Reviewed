# Simulated Annealing  

In **AI** and **computer science**, optimization problems are hard tasks to be solved. 
In particular, they can be found whenever parameters tuning is needed according to a *loss or gain function*:
they in fact consist in finding the optima of *objective functions* under certain constraints.

Other than well known mathematical structures, literature offers lots of valid different choices for the above mentioned computational analysis.
Inspired by nature and physics algorithms are for sure not the most efficient ones, but they are by far more curious and catchy [see ref. [3] for *Genetic algorithms*].

The project here is dedicated to the implementation of a fancy thermodynamics based iterative algorithm called *Simulated Annealing* written in *python* programming language: it allows the user to find global minima of given 2-variable real and non pathological functions.

## For the user
### Before getting started
The user is recommended to work with [*python 3.8*](https://www.python.org/downloads/release/python-383/), no preferred OS.
Libraries to be used: 
- [numpy](https://numpy.org/install/) 
- [mathplotlib](https://matplotlib.org/stable/users/installing.html)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [unittest](https://anaconda.org/anaconda/unittest2)

### How to 
The entire program is aimed to work in two different ways: it can operate in *demo* mode acting on four specific test functions or it can be applied on a specific user function either, to be written in a dedicated user-friendly *file.py*, already implemented with a default parabolic 2-D function. Also, all the parameters involved in the algorithm can be modified by the user itself via parsing.

- Clone the repository
- OPTIONAL: open [user_function.py](user_function.py), comment out the default function and write the new one to be passed
- On *Prompt command* digit:
  > python run.py 
  
  Optionals to be added after it:
  - >`-k` as `int` ->  Max number of iterations. [default: 1e6]
  - >`-m` as `str` -> If `userf` , perform the algorithm on the User function instead of the test ones, else omit it or write `test`
  - >`-o` as `Float` -> Objective function limit. [default: -1e10]
  - >`-r` as `Float` -> Reanniling tolerance value.[default: 100]
  - >`-v` as `bool` -> Verbose parameter, [default: False]
  - >`-t` as `Float` -> Initial temperature. [default: 100]
  - >`-ti` as `int` -> Number of iterations taken into account in Tolerance Energy. [default: 1000]
  - >`-tv` as `Float` -> Tolerance Energy value for stopping criterion [default: 1e-10]     
  
  
*Note: incorrect insertion, e.g. negative temperature or non `float` returned function values, will lead to assertion errors.*


### Testing
The repository includes a *unit_test.py* file that allows for the user to have a clear and optimized view of the algorithm and the core functions. It actually performs different tests on a very simple 2-D *energy* function of the form ***f(x)=x^2+y^2*** of which we know the behaviour and the exact minimum. This way it is possible to check whether if the algorithm works properly and the deterministic core functions are correct. Also, stochastic generations are controlled via *assertLessEqual/assertGreaterEqual* commands, in order for anything to result out of declared ranges.

To have the algorithm tested in terms of results validity, on *Prompt command* digit:
    > python unit_test.py

The system being stochastic implies test accurancy can't be 100% actually. Through central limit theorem and tries, the acceptability value for the minima to be registered as **correct** was set to be *delta == 1*


## Basics 
Simulated annealing (SA somewhere hereinafter) is a popular local search meta-heuristic used to address discrete
and, to a lesser extent, continuous optimization problems. The key feature of simulated annealing
is that it provides a means to escape local optima by allowing hill-climbing moves (i.e., moves
which worsen the objective function value) in hopes of finding a global optimum.

As an extension of the traditional ***Metropolis-Hastings*** algorithm, it is based on the use of **random search** in terms of a Markov chain: it can process and accept or reject solutions according to a certain probability function returns.

The name itself comes from direct comparison and analogies to the process of **physical
annealing with solids**, in which a crystalline solid is heated and then allowed to cool
very slowly until it achieves its most regular possible crystal lattice configuration (i.e., its
minimum lattice energy state), and thus is free of crystal defects. If the **cooling schedule**
is sufficiently slow, the final configuration results in a solid with such superior structural
integrity. 
Simulated annealing establishes the connection between this type of thermodynamic behavior and the search for global minima for a discrete optimization problem.

### Notation

Definition of involved parameters is essential for the user comprehension of code and algorithm itself.
Variables and functions come directly from physics:

- ***s***: current state or solution.
- ***e(s)***: specific free energy of ***s***.
- ***T***: current temperature.
- ***(s*)***: proposed new solution.
- ***Δe***: difference in free energy between states ***(s*)*** and ***s***.
- ***p(Δe, T)***: the acceptance probability function.

This should make the reader dip its toes into the strong correlation between subjects if the **minimisation principle of Gibbs free energy** is known.

## Algorithm Implementation

### [Steps](https://github.com/LMargotti/SACFAP_Exam/blob/main/algorithm.py)

1. Start from an initial random point ***s = s_0*** , with the initial temperature ***T = T_0***
2. Generate new candidate ***(s*)*** via definition of *move* (i.e., the change in position of ***s*** with related magnitude)
3. Compute the free energy difference ***Δe = e(s*) – e(s)***
4. Check for acceptance or rejection of ***(s*)*** according to the sign of ***Δe*** and to the value of ***p(Δe, T)***
5. Perform *temperature decreasing* via dedicated **cooling schedule**
6. Check whether if *re-annealing* is necessary or not
7. Repeat from *2* to *6* and run until stopping conditions are satisfied.

Despite lots of possibilities in terms of ways for the algorithm to be implemented, here the easiest and intuitive one is chosen, as it simply follows experimental physical reasoning: an *initial temperature* is set before the steps are run and it is changed if needed after step *4* only. This allows to have the *move* generation function, the **cooling schedule**, the *acceptance probability function* and the stopping criteria designed according to the user preferences.

The temperature ***T*** becomes an actual *control parameter* that influences both the **solution generation** and the **worsening move acceptance**: 
high values of ***T*** correspond to longer steps in the search space; gradually lowering them corresponds to restricting the "investigation area". Also, 
the **acceptance probability** for worsen solutions decreases sharply with ***T***: this gives SA the ability of escaping from local minima.

*Re-annealing* procedure is also used for escaping local minima, as it consists in restarting the search whenever a solution which is worse by a fixed amount than the best one found so far is reached.

### [Functions](https://github.com/LMargotti/SACFAP_Exam/blob/main/core_functions.py)
Simulated Annealing algorithm is here implemented for 2-dimensional space real functions with non-pathological behaviour.
Among the wide list of possibilities, **Boltzmann acceptance probability function** and **Geometric cooling** were chosen to define the probability ***p(Δe, T)*** and the **cooling schedule** respectively:

- ***p(Δe, T) = exp(- Δe/T)*** 


      def boltz_acceptance_prob(energy, new_energy, temperature):
    
        delta_e = new_energy - energy   
        if delta_e < 0 :
            return 1
        else:
            return np.exp(- delta_e / temperature)



- ***T_(k+1) = α T_(k)*** , with fixed ***α = 0.95***

      def geom_cooling(temp, k,  alpha = 0.95):

        return temp * alpha

        
Initial state (or solution) is generated uniformly random; the *move* lenght and direction are then evaluated to be proportional to the **square root of temperature** and randomized via generation of casual floating number in the [0,1] range. Note that it is necessary to have new solutions inside the function **domain**: clipping is then required and implemented as follows as a 1-D function that detects if the generated new solution coordinate overcomes boundaries and corrects it by substituting the non-valid entry with a random new one between the current state and the limit.

    def clip(x, interval, state):

        a,b = interval   
        if x < a :
            return rnd.uniform(a, state)    
        if x > b :
            return rnd.uniform(state, b)    
        else: 
            return x


In order to have the algorithm stopped, there's plenty of criteria to be implemented. 
Four different *stopping conditions* are here used: they're thought to be intuitive and easy to write.

1. Maximum number of iterations is reached (default value to be set *a priori*)
2. Temperature lower limit (***(T*=0)*** typically)
3. Minimum of free energy reached (strong dependence of function co-domain)
4. Tolerance value overcome

The latter is reported for clarity as it is the most frequently satisfied: the algorithm runs until the average change in value of the objective function 
is less than the tolerance.

    def tolerance(energies, tolerance, tolerance_iter) :

      if len(energies) <= tolerance_iter :
          return False
      if avg_last_k_value(energies, tolerance_iter) < tolerance :
          return True
      else : 
          return False

### Output 
After the algorithm is stopped, the following kind of output appears:

>Function: *function_name*

>Stopping criterion: *Crit_name*

>Number of iterations: *#iterations* as *int*

>Reanniling: *True_or_False*


### [Plots](https://github.com/LMargotti/SACFAP_Exam/blob/main/plot.py)
The system makes use of *matplotlib* library for graphics realization. 
Two different pictures are generated: the first one corresponds to the analized function(s) and the second is dedicated to **data analysis** and **results**.

As mentioned in the User dedicated subsection, the algorithm is performed on [**four specific test functions**](https://github.com/LMargotti/Simulated_Annealing_Exam/blob/main/test_functions.py) typically used in computer science:
- [Ackley function](https://en.wikipedia.org/wiki/Ackley_function)
- [Himmelblau function](https://en.wikipedia.org/wiki/Himmelblau%27s_function)
- [Rastrigin function](https://en.wikipedia.org/wiki/Rastrigin_function)
- [Rosenbrock function](https://en.wikipedia.org/wiki/Rosenbrock_function)

![](https://github.com/LMargotti/SACFAP_Exam/blob/main/images/test_fn.png?raw=true)

After the algorithm being executed correctly, final results are plotted. For test functions, actual global minima were added for comparison (black label).

![](https://github.com/LMargotti/SACFAP_Exam/blob/main/images/results.png?raw=true)

It is therefore possible to consider the system consistent with what expected but for few exceptions only: precise numerical method are suggested for best results.

## References
 1. Holger H. Hoos, Thomas Stützle, Stochastic Local Search, 2005
 2. Henderson, Darrall & Jacobson, Sheldon & Johnson, Alan. (2006). The Theory and Practice of Simulated Annealing.
 3. [*Genetic algorithms*](http://www.geneticalgorithms.it/) 
 




