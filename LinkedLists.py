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
        if self.head is None:   # Если список пуст
            print("Список пуст.")
            return

        if index == 0:          # Удаление первого узла
            self.head = self.head.next
            return

        current = self.head
        counter = 0
        while current.next and counter < index - 1:
            current = current.next
            counter += 1

        if current.next is None:  # Проверка выхода за границы
            print("Индекс вне диапазона.")
            return

        current.next = current.next.next  # Удаляем узел

    def insert_node(self, index, data):
        new_node = Node(data)   # Создаем новый узел
        if index == 0:          # Вставка в начало
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        counter = 0
        while current and counter < index - 1:
            current = current.next
            counter += 1

        if current is None:     # Проверка выхода за границы
            print("Индекс вне диапазона.")
            return

        new_node.next = current.next  # Связываем новый узел со следующим
        current.next = new_node       # Вставляем новый узел
            

newlinkedlist = LinkedList()
newlinkedlist.append(1)
newlinkedlist.append(2)
newlinkedlist.append(3)
newlinkedlist.append(4)
newlinkedlist.insert_node(0, 5)
newlinkedlist.print_list() #тут ты итак принтишь
