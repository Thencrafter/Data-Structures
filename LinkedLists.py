class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        ##Traversal of list
        while current.next:
            current = current.next
        current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
        print("None")

    def count_nodes(self):
        current = self.head
        counter = 0
        while current:
            counter += 1
            current = current.next
        return counter
    
    def delete_node(self, index):
        current = self.head
        counter = 0
        if index == 0:
            self.head = current.next
        else:
            while counter < index-1:
                current = current.next
                counter += 1
            current.next = current.next.next

    def insert_node(self, index, data):
        current = self.head
        new_node = Node(data)
        counter = 0
        if index == 0:
            self.head = new_node
            self.head.next = current
        else:
            while counter < index-1:
                current = current.next
                counter += 1
            new_node.next = current.next
            current = new_node
            

newlinkedlist = LinkedList()
newlinkedlist.append(1)
newlinkedlist.append(2)
newlinkedlist.append(3)
newlinkedlist.append(4)
newlinkedlist.insert_node(0, 5)
print(newlinkedlist.print_list())
