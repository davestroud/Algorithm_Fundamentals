def bubble_sort(items):
    for i in range(len(items)):
        already_sorted = True
        for j in range(len(items) - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j +1] = items[j+ 1], items[j]
                already_sorted = False
            if already_sorted:
                break
    return items