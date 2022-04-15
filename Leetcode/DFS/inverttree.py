def invertTree(self, root):
    if not root:
        return None
    
    root.right, root.left = (self.invertTree(root.left), self.invertTree(root.right))
    return root