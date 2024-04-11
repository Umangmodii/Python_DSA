def binary_search(list,low,high,n):
    
 if low <= high:
    mid = (low + high) // 2
        
    if list[mid] == key:
        return mid
        
    elif list[mid] > key:
        return binary_search(list,low,mid-1,n)
    
    else:
        return binary_search(list,mid+1,high,n)
    
 else:
    return -1


list = [10,20,30,40,50,60,70]
key = 60

n = len(list)

# using Divide & Conquer

result = binary_search(list,0,len(list)-1,n)

if result == -1:
    print("Not Found!")
   
else:
    print("Element Found at Index Position : ",result)