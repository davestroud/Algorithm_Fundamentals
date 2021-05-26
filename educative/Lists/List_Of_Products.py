def find_product(lst):
    # get product to start from left
    left = 1  
    product = []
    for ele in lst:
        product.append(left)
        left = left * ele 
    
    # get product starting from right
    right = 1
    for i in range(len(lst)-1, -1, -1):
        product[i] = product[i] * right
        right = right * lst[i]
    
    return product 


arr = [1,2,3,4]

print(find_product(arr))

