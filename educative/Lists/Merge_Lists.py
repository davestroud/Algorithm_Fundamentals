# My initial solution
def merge_lists(lst1, lst2):
    for x in list2:
         list1.append(x)
         list1.sort()
    return list1 
        
list1 = [1,3,4,5]  
list2 = [2,6,7,8]

print(merge_lists(list1,list2))