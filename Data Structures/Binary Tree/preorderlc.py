# Definition for a binary tree node.
class TreeNode():
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution():
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.trav(root, result)
        return result
    def trav(self, root, result):
        if root == None:
            return
        result.append(root.val)
        self.trav(root.left, result)
        self.trav(root.right, result)
        