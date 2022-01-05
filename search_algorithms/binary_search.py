"""
    Binary Search is a search algorithm that finds the position of a targeted value within a sorted array.
        - It is important that the given array is sorted for this algorithm to work accurately
        - It is known as a decrease and conquer algorithm because it decreases the array and tackles the subproblem
        - Best Time Complexity - O(1)
        - Average Time Complexity - O(log n)
        - Worst Time Complexity - O(n)
        - Space Complexity - O(1)
"""

def binary_search(variable_list, l, r, target):
    
    """
    Check the base case:
        Base case is:
            ** If the left index is less than or equal to the right index, continue to recursively search for the target value **
            
    Variables:
        l = left index
        r = right index
        middle = middle index
        variable_list = list of variables 
        target = targeted value
    """
    
    # IF left  index is less than right index, continue searching.
    if l <= r:
        middle = (l + r) // 2
        
        # if the middle value in the list equals target, then return index.
        if variable_list[middle] == target:
            return middle
        
        # if target value LESS THAN the current middle value of list, search the left half.
        elif target < variable_list[middle]:
            return binary_search(variable_list, l, middle-1, target)
        
        # if target value GREATER THAN the current middle value of list, search the left half.
        elif target > variable_list[middle]:
            return binary_search(variable_list, middle+1, r, target)
        
    # ELSE return -1
    else:
        return -1
    
"""
    Test binary search algorithm with the following lists and print results

        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        [2, 43, 66, 70, 100, 320, 450, 580, 670, 710]
        [23, 444, 1000, 5510]

"""   

test_list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
test_list2 = [2, 43, 66, 70, 100, 320, 450, 580, 670, 710]
test_list3 = [23, 444, 1000, 5510]

print("Binary Search Algorithm\n")

print("List 1: " + str(test_list1))
print("Index of 9: " + str(binary_search(test_list1, 0, len(test_list1), 9)) + "\n")

print("List 2: " + str(test_list2))
print("Index of 320: " + str(binary_search(test_list2, 0, len(test_list2), 320)) + "\n")

print("List 3: " + str(test_list3))
print("Index of 444: " +  str(binary_search(test_list3, 0, len(test_list3), 444)) + "\n")
    
    