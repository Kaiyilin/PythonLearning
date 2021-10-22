# Red-Black Tree implementation 

## Rule 1: Node was set to be assigned w/ colour properties (Black = 0, Red = 1)

## Rule 2: Existence of null leaf node, 
##         if you don't have value in the children node leave ass null

## Rule 3: If a node is Red both of its children must be black

## Rule 4: Root Node must be black

## Rule 5: The most critical one, 
##         every path from a node to its descedant null nodes,
##         must be contain the same number of black node


class Node(object):
    def __init__(self, value) -> None:
        # using the concept of pointer machine
        # a node shall have a pointer to its parent and children
        # all new insert Node was coloured in Red (1) 
        super().__init__()
        self.value = value
        self.parent = None 
        self.left = None
        self.right = None 
        self.colour = 1 

class RedBlackTree(object):
    
    def __init__(self):
        # Get a root quick
        self.TNULL = Node(0)
        self.TNULL.colour = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL

    def preorder_helper():
        return ""
    def balance(self):
        return ""

    def insert(self):
        return ""
    
    def delete(self):
        return """