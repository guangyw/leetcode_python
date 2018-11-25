# Definition for a binary tree node.
from Utils import TreeNode

class Solution:
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None:
            return t2
        elif t2 == None:
            return t1
        
        node = TreeNode(t1.val + t2.val)
        
        node.left = self.mergeTrees(t1.left, t2.left)
        node.right = self.mergeTrees(t1.right, t2.right)
        
        return node