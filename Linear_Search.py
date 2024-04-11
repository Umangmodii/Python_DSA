def linear_search(list,n,key):
    
    # Searching Elements
    for i in range(0,n):
        if list[i] == key:
            return i
    return -1
    
list = [10,20,30,40,50]
key = 30

n = len(list)
result = linear_search(list,n,key)

if result == -1:
    print("Element not Found!")
else:
    print("Elements found at : ",result)
