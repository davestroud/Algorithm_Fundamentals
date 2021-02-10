# def solution(data, n):
#     """A function that takes in a list of less than 100 integers
#         and a number n

#     Args:
#         data (list): The list should have no more than 100 integers.
#         n (integer): Number of scheduled assignments

#     Returns:
#         list: the same list, but with numbers that
#         occur more than (n) times removed entirely.
#     """
#    return n

# Would it be appropriate to use Collections to take in the list?
# https://stackabuse.com/introduction-to-pythons-collections-module/

# def solution(data, n):
    # if > 100 integers, pass
    # else 
            #return the same list
            # remove integers that occur
def solution(data, n):
    newlist = data
    if len(data) > max(data):
        length = len(data)
    else:
        length = max(data)
    for i in range(length+1):
        if data.count(i) > n:
            for x in range(data.count(i)):
                newlist.remove(i)
    return newlist

# https://github.com/atreids/foobar-minions/blob/master/solution.py