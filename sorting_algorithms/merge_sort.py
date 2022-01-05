"""
    Merge Sort is a sorting algorithm that divides an unsorted list into halves until it has n sublists and 
    then merges the list into sorted halves until it is one complete and sorted list.
        - It is known as a Divide and Conquer algorithm because it divides an array or list and conquers the subproblem
        - Best Time Complexity - O(n*log(n))
        - Average Time Complexity - O(n*log(n))
        - Worst Time Complexity - O(n*log(n))
        - Space Complexity - n
"""

def merge_sort(arr):
    
    """
    Part 1: halve list into sublists until length of sublist is 1
            
    Variables:
        middle = middle value of list
        left = left split list
        right = right split list
        arr = list of variables
        
    
    1. Check the base case:
        Base case is:
            ** If the length of the list is greater than 1, continue splitting list. **
            
    2. Split list into left list and right list down the middle
    
    3. Send left split list into merge_sort
    
    4. Send right split list into merge_sort
    """

    if len(arr) > 1:
        # find the middle of the list
        middle = len(arr) // 2

        # divide the lists into a left and right list
        left = arr[:middle]
        right = arr[middle:]
        
        merge_sort(left)
        merge_sort(right)
        
        """
        Part 2: Sort list by merging them into halves until one complete list
        
           Variables:
                i = left split index
                j = right split index
                k = new sorted list/array index
                
            1st while loop:
                Continue while loop that will iterate thru left split and right split list until index i or index j is
                larger or equal to length of their respective lists.
                
            2nd while loop:
                Loop that will iterate thru left split list incase i is still less than length of left list
                
                
            3rd while loop:
                Loop that will iterate thru right split list incase j is still less than length of right list
                
            return sorted list
        """
        
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
                
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        
        return arr
    
"""
    Test merge sort algorithm with the following lists and print results

        [12, 11, 13, 5, 6, 7]
        [6, 5, 12, 10, 9, 1]

"""   

test_list1 = [12, 11, 13, 5, 6, 7]
test_list2 = [6, 5, 12, 10, 9, 1]

print("Merge Sort Algorithm\n")

print("List 1: " + str(test_list1))
test_list1 = merge_sort(test_list1)
print("Sorted List 1: " + str(test_list1) + "\n")
    

print("List 2: " + str(test_list2))
test_list2 = merge_sort(test_list2)
print("Sorted List 2: " + str(test_list2) + "\n")
    