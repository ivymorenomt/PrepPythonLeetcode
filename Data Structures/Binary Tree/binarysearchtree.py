class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None # this is if the root is null
    def add(self, current, value):
        if self.root == None:
            self.root = Node(value) # you are going to add a new Node value
        else:
            if value < current.value: # current will start as root node
                if current.left == None:
                    current.left = Node(value)
                else:
                    self.add (current.left, value)
            else:
                if current.right == None:
                    current.right = Node(value)
                else:
                    self.add(current.right, value)

