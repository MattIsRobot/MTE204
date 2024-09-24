from ErrorCalculation import *
from prettytable import PrettyTable
import math


class BoundsException(Exception):
    pass

def estimateRoot(xi, f, fPrime):
    fVal = f(xi)
    fDVal = fPrime(xi)
    return (xi-(fVal/fDVal), fVal, fDVal)

def doIterations(guess, function, functionDerivative, numIterations=20) -> list[list]:
    lastEstimate = guess
    table = []

    for i in range(numIterations):
        xNext, fVal, fDVal = estimateRoot(lastEstimate, function, functionDerivative)

        # Calculate error
        approxErr = calcError(lastEstimate, xNext)
        
        # Print table
        tableRow = [str(i+1), lastEstimate, fVal, fDVal, xNext, approxErr]
        table.append(tableRow)
        
        lastEstimate = xNext

    tab = PrettyTable(['Iteration', 'xi', 'f(xi)', 'f\'(xi)', 'xi+1', 'Ea'])
    tab.add_rows(table[0:])
    print(tab)
    return table