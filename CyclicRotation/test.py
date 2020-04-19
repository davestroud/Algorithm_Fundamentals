e# import random

# SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
#          'Jack', 'Queen', 'King', 'Ace']

# rank = random.randrange(0, len(RANKS))
# suit = random.randrange(0, len(SUITS))

# A = [3, 8, 9, 7, 6]
# K = 3

def solution(A, K): # input parameters
    l = len(A) # l = the length of A: 5, in this scenerio
    if l < 2: # if 5 is less than 2
        return A # return [3, 8, 9, 7, 6]
    elif l == K:
        return A
    else:
        B = [0] * l
        for i in range(l):
            B[(i+K)%l] = A[i]
        return B



    
print(solution([3,8,9,7,6], 3))
