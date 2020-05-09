import sys
import random

# Accept integer command-line arguments stake, goal, trialCount.
# Run trialCount experiments that start with stake dollars and
# terminate on 0 dollars or goal. Write to standard output the
# percentage of wins and the average number of bets per experiment.

stake = int(sys.argv[1])
goal = int(sys.argv[2])
trials = int(sys.argv[3])

# Run trailCount experiments that start with stake and terminate on
# 0 or goal
