# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def preorder(node, binary):
            if not node: 
                return 0
            if not node.left and not node.right: 
                return int(binary+str(node.val),2)
            else:
                return preorder(node.left, binary+str(node.val)) + preorder(node.right, binary+str(node.val))
        return preorder(root, "")