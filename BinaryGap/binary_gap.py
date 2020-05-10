# Binary Gap problem

# A binary gap within a positive integer N is any maximal sequence of
# consectutive zeros surrounded by ones at both ends in the binary
# representation of N.
#
# For example, number 9 has binary representation 1001 and contains a binary
# gap of length 2. The number 529 has binary representation 1000010001 and
# contains two binary gaps: one of length 4 and one of length 3. The number
# 20 has binary representation 10100 and contains one binary gap of length 1.
# The number 15 has binary representation 1111 and has no binary gaps.
# The number 32 has binary representation 100000 and has no binary gaps.
#
# Write a function:
#
# def solution (N)
# that, given a positive integer N, returns the length of its longest binary
# gap. The function should return 0 if N doesn't contain a binary gap.
#
# For example, given N = 1041 the function should return 5, because N has
# binary representation 10000010001 and so its longest binary gap is of length 5.
# Given N = 32 the function should return 0, because N has binary
# representation '100000' and thus no binary gaps.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [1..2,147,483,647]. ~ This number
# represents the maximum positive value for a 32-bit signed binary integer.

# Code Walkthrough
# Using best programing practices, we will put our algorithm into a function
# named solution.
#
# The bin()method in Python converts and returns the binary equivalent string
# of a given integer.
# bin(9) note that we are given a sting that needs to be converted to a number.


def solution(N):
    bin_rep = str(bin(N))[2:] # Conversion of strings to number for input.
    bin_gap = False # Initilize to false
    bin_max = 0 # Initialize bin_max to 0
    bin_counter = 0 # Initialize bin_counter to 0
    for symbol in bin_rep:
        if symbol == '1':
            if bin_max < bin_counter:
                bin_max = bin_counter
            bin_gap = True
            bin_counter = 0
        elif bin_gap:
            bin_counter += 1
    return bin_max

# Mechanics of the for loop
# Each time the digit is 1, bin_counter will be updated
# If it is bigger than the previous biggest one, then bin_max is updated
# The final return is with bin_max

# print(solution(1041))


# Complexity:
# Expected worst-case time complexity it O(log(N))
# Expected worst-case space complexity is O(1)

# Link to understanding control flow of functions:
# https://introcs.cs.princeton.edu/python/21function/
