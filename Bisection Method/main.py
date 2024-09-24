from Bisection import doBisectionIterations
import math

def water(x):
    g = 9.81
    h = x
    L = 4
    t = 2.5
    return math.sqrt(2*g*h)*math.tanh(math.sqrt(2*g*h)*t/(2*L))-5

doBisectionIterations(0,2, water, 10)

