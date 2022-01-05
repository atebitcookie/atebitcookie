import random

"""
    Linked List Data Structure
        - Linear data structure
        - Stores data non-contiguously 
        - Need to traverse to find elements
            - O(n) traversal complexity
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_List:
    def __init__(self):
        self.head = None
        
    def print_list(self):
        temp_pointer = self.head
        while(temp_pointer):
            print(temp_pointer.data)
            temp_pointer = temp_pointer.next
            
    def insert_data(self, data):
        new_node = Node(data)
        if(self.head):
            current_node = self.head
            while(current_node.next):
                current_node = current_node.next
            current_node.next = new_node
        else:
            self.head = new_node
    
if __name__ == '__main__':
    
    linked_list = Linked_List()
   
    # build list
    n = random.randint(1, 20)
    print("Random int: " + str(n))
    
    while(n > 0):
        linked_list.insert_data(n)
        n -= 1
        
    linked_list.print_list()