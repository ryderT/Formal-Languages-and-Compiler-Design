limit = 0


class Node:
    def __init__(self, id, info):
        self.left = None
        self.right = None
        self.id = id
        self.info = info
    def __str__(self):
        return "[" + str(self.id) + "," + str(self.info) + "]"


class SymbolTable:
    def __init__(self):
        self.root = None
    def __str__(self):
        return self.preoderTraversal(self.root)
        
    def preoderTraversal(self,node:Node):
        string = ""
        if node != None:
            string += str(node) + ': '
            string += 'left: ' + str(node.left) + ' '
            string += 'right: ' + str(node.right) + ' '
            string += '\n'
            string += self.preoderTraversal(node.left)
            string += self.preoderTraversal(node.right)
        return string
        
    def insert(self, value):
        global limit
        if self.root is None:
            limit += 1
            self.root = Node(limit, value)
        else:
            parent = None
            left, right = False, False
            node = self.root
            while node is not None:
                parent = node
                if node.info < value:
                    node = node.left
                    left, right = True, False
                elif node.info > value:
                    node = node.right
                    left, right = False, True
            if left == True:
                limit += 1
                parent.left = Node(limit, value)
            else:
                limit += 1
                parent.right = Node(limit, value)

    def search(self, value):
        if self.root is None:
            return None
        node = self.root
        while node is not None:
            if node.info == value:
                return node
            elif node.info < value:
                node = node.left
            else:
                node = node.right
        return None
