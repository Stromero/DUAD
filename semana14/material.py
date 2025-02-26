# CTRL + K + C para comentar todo un bloque de codigo
# CTRL + K + U para descomentar un bloque de codigo

# class Node:
#     data:str
#     next:"Node"

#     def __init__(self, data, next=None):
#         self.data = data
#         next = next

# class LinkedList:
#     head:Node

#     def __init__(self,head):
#         self.head = head
    
#     def print_structure(self):
#         current_node = self.head
#         print(current_node.data)

# third_node = Node('I am the first node')
# second_node = Node('I am the second node', third_node)
# first_node = Node('I am the first node',second_node)

# linked_list = LinkedList(first_node)
# linked_list.print_structure()

#***********************************************************
#Imprimir el segundo nodo
#***********************************************************

# class Node:
#   data: str
#   next: "Node"

#   def __init__(self, data, next=None):
#     self.data = data
#     self.next = next

# class LinkedList:
#   head: Node

#   def __init__(self, head):
#     self.head = head

#   def print_structure(self):
#     current_node = self.head
    
#     while (current_node is not None):
#       print(current_node.data)
#       current_node = current_node.next



# third_node = Node("Soy el tercer nodo")
# second_node = Node("Soy el segundo nodo", third_node)
# first_node = Node("Soy el primer nodo", second_node)

# linked_list = LinkedList(first_node)
# linked_list.print_structure()

#*************************************************************************
#Creation of Queue
#*************************************************************************

class Node:
    data : str
    next : 'Node'

    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
class Queue:
    head : Node

    def __init__(self, head):
        self.head = head
    
    def print_structure(self):
        current_node = self.head

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    #Para agregar nodos al final
    def enqueue(self, new_node):
        current_node = self.head

        while current_node.next is not None:
            current_node = current_node.next
        
        current_node.next = new_node
    
    # dequeue para quitar nodos (del inicio)
    def dequeue(self):
        if self.head:
            self.head = self.head.next

first_node = Node('Hello')
my_queue = Queue(first_node)

second_node = Node('World')
my_queue.enqueue(second_node)

third_node = Node('third')
my_queue.enqueue(third_node)

forth = Node('forth')
my_queue.enqueue(forth)

my_queue.print_structure()

print('DEQUEUE')

my_queue.dequeue()
my_queue.print_structure()

print('DEQUEUE')

my_queue.dequeue()
my_queue.print_structure()

print("DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()

print("DEQUEUE")

my_queue.dequeue()
my_queue.print_structure()

print('DEQUEUE')

my_queue.dequeue()
my_queue.print_structure()




