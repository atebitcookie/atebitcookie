class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        return self.stack.pop()
    
    def get_size(self):
        return len(self.stack)
    
    def print_stack(self):
        print(self.stack)
    

if __name__ == '__main__':
    stack = Stack()
    stack.print_stack()
    stack.push(4)
    stack.print_stack()
    stack.push(15)
    stack.print_stack()
    stack.push(33)
    stack.print_stack()
    stack.pop()
    stack.print_stack()