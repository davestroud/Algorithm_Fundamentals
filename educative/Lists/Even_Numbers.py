def remove_even(lst):
    odds = []
    for number in lst:
        if number % 2 != 0:
            odds.append(number)
    return odds

print(remove_even([3, 2, 41, 3, 34]))


# List comprehension method
def remove_even(lst):
    return [number for number in lst if number % 2 != 0]

print(remove_even([3, 2, 41, 3, 34]))