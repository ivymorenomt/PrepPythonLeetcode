def flatten(self, root):
    def dfs(root):
        if not root:
            return None
        # flatten the tree
        
        leftTail = dfs(root.left)
        rightTail = dfs(root.right)
        
        if root.left:
            leftTail.right = root.right
            root.right = root.left
            root.left = None
        last = rightTail or leftTail or root
        return last
    dfs(root)