#1. Cree una estructura de objetos que asemeje un Stack.
#    1. Debe incluir los métodos de `push` (para agregar nodos) y `pop` (para quitar nodos).
#    2. Debe incluir un método para hacer `print` de toda la estructura.
#    3. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    value : str
    nextNode: 'Node'

    def __init__(self,value,nextNode=None):
        self.value = value
        self.nextNode = nextNode

class Stack:
    #size : int
    firstNode : Node

    def __init__(self):
        self.firstNode = None
    
    def push(self, value):
        self.firstNode = Node(value, nextNode=self.firstNode)
    
    def pop(self):
        if self.firstNode is None:
            print('The stack is empty')
        else:
            element_to_be_removed = self.firstNode.value
            self.firstNode = self.firstNode.nextNode
            return print(f'The element is being removed is: {element_to_be_removed}')

    def get(self) -> str:
        if self.firstNode is None:
            print('The stack is empty')
        else:
            return self.firstNode.value

    def print_structure(self):
        current_node = self.firstNode

        while current_node is not None:
            print(current_node.value)
            current_node = current_node.nextNode
    

my_stack = Stack()
my_stack.get()
my_stack.pop()
my_stack.push('Hi')
my_stack.push('I am Steven')
my_stack.push('and')
my_stack.push('learning coding in lyfter team is so cool')
my_stack.print_structure()
my_stack.pop()
my_stack.pop()
my_stack.print_structure()


