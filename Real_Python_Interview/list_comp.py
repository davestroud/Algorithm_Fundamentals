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