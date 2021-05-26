def find_product(lst):
    left = 1
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele 
    
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]
    
    return product 


arr = [1,2,3,4]

print(find_product(arr))

