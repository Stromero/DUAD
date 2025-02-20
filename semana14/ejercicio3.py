#3. Cree una estructura de objetos que asemeje un Binary Tree.
#    1. Debe incluir un método para hacer `print` de toda la estructura.
#    2. No se permite el uso de tipos de datos compuestos como `lists`, `dicts` o `tuples` ni módulos como `collections`.

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, value):
        def _insert_recursive(current, value):
            if value < current.value:
                if current.left is None:
                    current.left = Node(value)
                else:
                    _insert_recursive(current.left, value)
            else:
                if current.right is None:
                    current.right = Node(value)
                else:
                    _insert_recursive(current.right, value)
        
        _insert_recursive(self.root, value)

    def print_tree(self):
        def _print_recursive(node, depth=0):
            if node is not None:
                _print_recursive(node.right, depth + 1)
                print("    " * depth + str(node.value))
                _print_recursive(node.left, depth + 1)
        
        _print_recursive(self.root)


tree = BinaryTree(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(18)

tree.print_tree()
