class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop (self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
def reverse_string(string):
    stack = Stack()
    for i in string:
        stack.push(i)
    reversed_string = ""
    while not stack.is_empty():
        reversed_string += stack.pop()
    return reversed_string

def is_polyndrome(string):
    return string == reverse_string(string)

print(is_polyndrome("rdsaw"))