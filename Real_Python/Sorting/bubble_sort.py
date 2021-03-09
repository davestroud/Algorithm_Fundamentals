def bubble_sort(items):
    for i in range(len(items)): # Iterate through whole list
        already_sorted = True # Set break condition
        for j in range(len(items) - i - 1): # Maintain a growing section of the list that is sorted
            if items[j] > items[j + 1]: # Swap all out of place items.
                items[j], items[j + 1] = items[j + 1], items[j]
                already_sorted = False # Set sorted to false if we needed to swap
        if already_sorted:
            break
    return items

items = [1, 2, 5, 2, 3, 8, 1]
print(bubble_sort(items))
