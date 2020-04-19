#-----------------------------------------------------------------------
# harmonicf.py
#-----------------------------------------------------------------------

import sys

def harmonic(n):
    total = 0.0
    for i in range(1, n+ 1):
        total += 1.0 / float(i)
    return total

# Write to standard output the harmonic numbers specified as
# command-line arguments.

for j in range(1, len(sys.argv)):
    arg = int(sys.argv[j])
    value = harmonic(arg)
    print(value)

#-----------------------------------------------------------------------

# python harmonicf.py 1 2 4
# 1.0
# 1.5
# 2.083333333333333

# python harmonicf.py 10 100 1000 10000
# 2.9289682539682538
# 5.187377517639621
# 7.485470860550343
# 9.787606036044348