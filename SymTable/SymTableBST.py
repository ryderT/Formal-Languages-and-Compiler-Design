limit = 0


class Node:
    def __init__(self, id, info):
        self.left = None
        self.right = None
        self.id = id
        self.info = info


class SymbolTable:
    def __init__(self):
        self.root = None

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
                if node.val < value:
                    node = node.left
                    left, right = True, False
                elif node.val > value:
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
            if node.val == value:
                return node
            elif node.val < value:
                node = node.left
            else:
                node = node.right
        return None