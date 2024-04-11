# The selection sort algorithm sorts an array by repeatedly finding the minimum element

def Selection_Sort(array):

    length = len(array)
    
    for i in range(length - 1):    
        min = i
        
        for j in range(i+1, length):
            if array[j] < array[min]:
                min = j
                
            array[i],array[min] = array[min],array[i]
                
    return array

array = [21,6,9,33,3]  
  
print("The sorted array is: ", Selection_Sort(array))  