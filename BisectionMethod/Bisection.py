from ErrorCalculation import *
from prettytable import PrettyTable
import math


class BoundsException(Exception):
    pass

def estimateRoot(f, lowerBound, upperBound) -> tuple:
    lVal = f(lowerBound)
    uVal = f(upperBound)
    if lVal * uVal >= 0: 
        raise BoundsException

    # Estimate the root as the midsection
    rootEst = (upperBound - lowerBound) / 2 + lowerBound
    cVal = f(rootEst)

    return (lowerBound, upperBound, rootEst, lVal, uVal, cVal)

def updateBounds(lowerBound, upperBound, estimate, lVal, uVal, cVal):
    if cVal == 0: 
        return (lowerBound, upperBound)
    elif cVal * lVal < 0: 
        return (lowerBound, estimate)
    elif cVal * uVal < 0: 
        return (estimate, upperBound)
    raise BoundsException

def doBisectionIterations(lBound, uBound, function, numIterations=20, desiredError=None) -> list[list]:
    lastEstimate = None
    table = []

    if desiredError != None:
        numIterations = iterationsForDesiredError(lBound, uBound, desiredError)
    for i in range(numIterations):
        iterationRow = estimateRoot(function, lBound, uBound)
        lBound, uBound = updateBounds(*iterationRow)

        # Calculate error
        approxErr = calcError(lastEstimate, iterationRow[2])
        lastEstimate = iterationRow[2]
        
        # Print table
        tableRow = [str(i+1)]
        tableRow.extend([str(v) for v in iterationRow])
        tableRow.append(approxErr)
        table.append(tableRow)

    tab = PrettyTable(['Iteration', 'xL', 'xU', 'xR', 'f(xL)', 'f(xU)', 'f(xR)', 'Ea'])
    tab.add_rows(table[0:])
    print(tab)
    return table

def iterationsForDesiredError(lBound, uBound, desiredError) -> int:
    return math.ceil(math.log2((uBound-lBound)/desiredError))