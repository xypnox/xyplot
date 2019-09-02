import numpy as np


def evalCurve(a, const, polyDeg=1):
    """
    Evaluates value of curve at x=a for given const of polyDeg degree polynomial
    """
    return sum([const[i]*a**(polyDeg-i) for i in range(polyDeg+1)])


def getNumArrange(x, depth=1000, extend=1):
    """
    Returns a numpy array for with depth # of divisions within the eq
    extend can be passed to extend the range with the ratio of the extension
    """
    a, b = min(x), max(x)
    a, b = a + (a - extend*a), extend*b
    return np.arange(a, b, (b-a)/depth)


def getCurve(x, y, polyDeg=1, depth=1000, extend=1):
    """
    Returns x, y, constants so that they are smooth plotable polynomial curve
    By default the function returns values for a linear polynomial
    """
    const = np.polyfit(x, y, polyDeg)
    x_o = getNumArrange(x, depth, extend)
    return x_o, np.array([evalCurve(a, const, polyDeg) for a in x_o]), const
