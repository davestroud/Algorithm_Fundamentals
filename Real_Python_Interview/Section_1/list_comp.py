lst = [1, 2, -5, 4]

# 1st methoud
def square(x):
    return x * x

list(map(square, lst))

# 2nd method
result = []
for num in lst:
    result.append(square(num))
    
# 3rd method ~ list comprehension
[square(num) for num in lst]

##################################################
# Interview type problem using list comprehensions
#################################################

# Standard method
grid = [[0, 0, 0],
        [0, 0, 0]]

num_rows = 2
num_columns = 3

grid = []

for _ in range(num_rows):
    curr_row = []
    for _ in range(num_columns):
        curr_row.append(0)
    grid.append(curr_row)
   
grid

# List comprehension
grid1 = [[0 for _ in range(num_columns)] for _ in range(num_rows)]
grid1


''' Max, min, any
    lst = [1, 2, -5, 4]
'''
# Returns min and max square root
max(lst, key=lambda x: x * x)
min(lst, key=lambda x: x * x)

# checks if any of the numbers in list are odd
# note the any and all function don't take in a 
# key value
any([(lambda x: x % 2 ==1)(num) for num in lst])
all([(lambda x: x % 2 ==1)(num)for num in lst])