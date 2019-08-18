# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def btreeGameWinningMove(self, root: TreeNode, n: int, x: int) -> bool:
        sizes = []
        
        def findNumbers(node, x):
            if not node:
                return 0
            
            l = findNumbers(node.left, x)
            r = findNumbers(node.right, x)
            
            if node.val == x:
                sizes.extend([l, r])
            
            return 1 + l + r
        
        findNumbers(root, x)
        
        return max(n - sum(sizes) - 1, max(sizes)) > n / 2