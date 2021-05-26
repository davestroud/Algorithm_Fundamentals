# My initial solution
def merge_lists(lst1, lst2):
    for x in lst2:
         lst1.append(x)
         lst1.sort()
    return lst1 
        
lst1 = [1,3,4,5]  
lst2 = [2,6,7,8]

print(merge_lists(lst1,lst2))