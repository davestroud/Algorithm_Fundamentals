#-----------------------------------------------------------------------
# gauss.py
#-----------------------------------------------------------------------

import sys
import math

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean 0.0
# and standard deviation 1.0 at the given x value.

def phi(x):
    return math.exp(-x * x / 2.0) / math.sqrt(2.0 * math.pi)

#-----------------------------------------------------------------------

# Return the value of the Gaussian probability function with mean mu
# and standard deviation sigma at the given x value.

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma

#-----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean 0.0 and standard deviation 1.0 at the given z value.

def Phi(z):
    if z < -8.0:
        return 0.0
    if z > 8.0:
        return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2
    return 0.5 + phi(z) * total

#-----------------------------------------------------------------------

# Return the value of the cumulative Gaussian distribution function
# with mean mu and standard deviation sigma at the given z value.

def cdf(z, mu=0.0, sigma=1.0):
    return Phi((z - mu) / sigma)

#-----------------------------------------------------------------------

# Accept floats z, mu, and sigma as command-line arguments. Use them
# to test the cdf() and pdf() functions. Write the
# results to standard output.

z = float(sys.argv[1])
mu = float(sys.argv[2])
sigma = float(sys.argv[3])

print(cdf(z, mu, sigma))

#-----------------------------------------------------------------------

# python gauss.py 820 1019 209
# 0.17050966869132106

# python gauss.py 1500 1019 209
# 0.9893164837383885

# python gauss.py 1500 1025 231
# 0.9801220907365491