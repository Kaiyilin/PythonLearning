# BinarySearchTree

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        self.recursive_insert(self.root, new_val)
        
    def recursive_insert(self, start, new_val):
        """
        if start value < new_val move to right, 
        if the right side exist, do the function one more time,
        otherwise make it a Node(with empty branch for future insert)
        Same condition for start value > new_val only if goes to the left
        """
        if start.value < new_val:
            if start.right:
                self.recursive_insert(start.right, new_val)
            else:
                start.right = Node(new_val)
        else:
            if start.left:
                self.recursive_insert(start.left, new_val)
            else:
                start.left = Node(new_val)
        return

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        return self.Bi_search(self.root, find_val)

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        
        return self.preorder_print(self.root, "")[:-1]

    def binary_search(self, start, find_val):
        """Helper method - use this to create a recursive search solution.
        
        If start.value == find_val we nailed it 
        start.value < find_val search the right branch
        start.value > find_val search the left branch
        Otherwise return False
        """
        # if 
        if start:
            if start.value == find_val:
                return True
            elif start.value < find_val:
                return self.binary_search(start.right, find_val)
            else:
                return self.binary_search(start.left, find_val)
        return False

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a 
        recursive print solution."""
        if start:
            traversal += str(start.value) + "-"
            # go left, if the child still have left branch, it'll continue go left
            traversal = self.preorder_print(start.left,traversal)
            # go right, until the node finish it's left side
            traversal = self.preorder_print(start.right,traversal)
        return traversal
# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

print(tree.print_tree())
# Check search
# Should be True
print(tree.search(4))
# Should be False
print (tree.search(6))