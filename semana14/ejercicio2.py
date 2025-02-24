# 2. Cree una estructura de objetos que asemeje un Double Ended Queue.
#    1. Debe incluir los métodos de `push_left` y `push_right` (para agregar nodos al inicio y al final) y `pop_left` y `pop_right` (para quitar nodos al inicio y al final).
#    2. Debe incluir un método para hacer `print` de toda la estructura.
#    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.
# https://www.geeksforgeeks.org/implementation-deque-using-doubly-linked-list/


class Node:
    value : str
    next : None
    prev : None

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Deque:
    head : Node
    tail : Node

    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_deque(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    def push_left(self,value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def push_right(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def pop_left(self):
        if not self.head:
            print('Deque structure is empty')
            return None
        value = self.head.value
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        return print(f'The node is being remove left side is: {value}')
    
    def pop_right(self):
        if not self.tail:
            print('Deque structure is empty')
            return None
        value = self.tail.value
        self.tail = self.tail.prev
        if self.tail:
            self.tail.next = None
        else:
            self.head = None
        return print(f'The node is being remove from right side is: {value}')
    

my_structure = Deque()
my_structure.pop_left()
my_structure.push_left('hi')
my_structure.push_right('my')
my_structure.push_left('name')
my_structure.push_right('is')
my_structure.push_left('Steven')
my_structure.print_deque()
my_structure.pop_left()
my_structure.pop_right()
my_structure.print_deque()