"""
    Merge Sort is a simple sorting algorithm that repeatedly swaps adjacent elements if they are out of order.
        - Best Time Complexity - O(n) where list is already sorted
        - Average Time Complexity - O(n^2)
        - Worst Time Complexity - O(n^2)
        - Space Complexity - O(1)
"""

def bubble_sort(arr):
    
    """
        Variables:
            arr_length = length of given array
            swapped = if adjacent elements where switched or not
            i = index of arr_length
    """

    arr_length = len(arr)
    
    for i in range(arr_length):
        swapped = False
        
        for j in range(0, arr_length-i-1):
            # if current element greater than next element then swap
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
                
        if swapped == False:
            break
        
    return arr
    
"""
    Test bubble sort algorithm with the following lists and print results

        [12, 11, 13, 5, 6, 7]
        [6, 5, 12, 10, 9, 1]

"""   

test_list1 = [12, 11, 13, 5, 6, 7]
test_list2 = [6, 5, 12, 10, 9, 1]

print("Bubble Sort Algorithm\n")

print("List 1: " + str(test_list1))
test_list1 = bubble_sort(test_list1)
print("Sorted List 1: " + str(test_list1) + "\n")
    

print("List 2: " + str(test_list2))
test_list2 = bubble_sort(test_list2)
print("Sorted List 2: " + str(test_list2) + "\n")
    