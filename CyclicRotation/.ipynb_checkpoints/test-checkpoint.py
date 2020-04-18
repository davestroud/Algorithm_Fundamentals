# import random

# SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
# RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10',
#          'Jack', 'Queen', 'King', 'Ace']

# rank = random.randrange(0, len(RANKS))
# suit = random.randrange(0, len(SUITS))


def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)