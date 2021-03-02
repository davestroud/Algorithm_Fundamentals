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
    