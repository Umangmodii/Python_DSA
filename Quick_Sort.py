# QuickSort is a divide and conquer algorithm. It picks an element as a pivot and partitions the given array around the picked pivot.

# There are many different versions of quickSort that pick pivot in different ways. 

# Always pick the first element as a pivot
# Always pick the last element as a pivot
# Pick a random element as a pivot
# Pick median as a pivot

def partition(list,low,high):
    
    pivot = list[high]
    
    i = low - 1
    
    for j in range(low,high):
        if list[j] <= pivot:
            
            i = i + 1
            
            (list[i],list[j]) = (list[j],list[i])
            
    (list[i+1],list[high]) = (list[high],list[i+1])          
              
    return i + 1

def Quick_Sort(list, low, high):
    
    if low < high:
        p = partition(list,low,high)
    
         # Recursive call on the left of pivot
        Quick_Sort(list,low,p-1)
        
        Quick_Sort(list,p + 1, high)
    
list = [1, 7, 4, 1, 10, 9, -2]

print("Unsorted List is : ",list)

size = len(list)

Quick_Sort(list,0,size-1)

print("Sorted List is : ",list)