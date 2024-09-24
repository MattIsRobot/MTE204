from Bisection import doBisectionIterations

def shiftedParabola(x):
    return (x**2)-1.3

doBisectionIterations(0,2, shiftedParabola, 2, 0.00003)

