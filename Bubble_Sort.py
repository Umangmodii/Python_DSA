# Swapping Technique Used in Python

def bubble_sort(list):
    
    for i in range(0, len(list)-1):
        for j in range(len(list)-1):
            
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
                
    return list

list = [5, 3, 8, 6, 7, 2] 

print("The Unsorted List is : ",list)

# Calling a Method in Bubble_Sort
print("The Sorted List is : ",bubble_sort(list))