import sys
import math

# Return the value of the Gaussian probability function with mean 0.0
# and standard deviation of 1.0 at the given x value.

def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma
