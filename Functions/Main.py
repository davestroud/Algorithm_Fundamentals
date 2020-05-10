# Simple function


def my_function(x):
    return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
# -----------------------------------------------------------

# Return value with list


def my_list(food):
    for x in food:
        print(x)


fruits = ['apple', 'banana', 'cherry']

# print(my_list(fruits))

# -----------------------------------------------------------

# Recursion
"""
Python also accepts function recursion, which means a defined function can call
itself.

Recursion is a common mathematical and programming concept. It means that a
function calls itself. This has the benefit of meaning that you can loop through
 data to reach a result.

The developer should be very careful with recursion as it can be quite easy to
slip into writing a function which never terminates, or one that uses excess
amounts of memory or processor power. However, when written correctly recursion
can be a very efficient and mathematically-elegant approach to programming.

"""

def recursion(k):
    if(k > 0):
        result = k + recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
recursion(6)
