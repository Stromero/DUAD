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
        #self.size = 0
        self.firstNode = None
    
    def push(self, value):
        self.firstNode = Node(value, nextNode=self.firstNode)
        #self.size += 1
    
    def pop(self):
        self.firstNode = self.firstNode.nextNode
        #self.size -= 1

    def get(self) -> str:
        return self.firstNode.value
    
    # def getSize(self) -> int:
    #     return self.size

my_stack = Stack()
my_stack.push('Hi')
print(my_stack.get())
my_stack.push('I am Steven')
print(my_stack.get())
my_stack.push('and')
print(my_stack.get())
my_stack.push('learning coding in lyfter team is so cool')
print(my_stack.get())
my_stack.pop()
print(my_stack.get())
my_stack.pop()
print(my_stack.get())
my_stack.pop
print(my_stack.get())


