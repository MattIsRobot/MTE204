from NewtonRaphson import doIterations
import math

def func(x):
    return (x**5) - 16.05*(x**4) + 88.75*(x**3) - 192.0375*(x**2) + 116.35*x + 31.6875

def derivative(x):
    return 5*(x**4) - 16.05*4*(x**3) + 88.75*3*(x**2) - 192.0375*2*(x) + 116.35


doIterations(0.5825, func, derivative, 8)

