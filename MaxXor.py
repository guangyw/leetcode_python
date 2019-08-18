class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MaxXor:
    def buildTree(self, arr):
        root = TreeNode(0)
        for num in arr:
            curNode = root
            for i in range(31, -1, -1):
                if num & 1 << i == 1:
                    if curNode.left == None:
                        curNode.left = TreeNode(1)
                    curNode = curNode.left
                else:
                    if curNode.right == None:
                        curNode.right = TreeNode(0)
                    curNode = curNode.right
        return root

    def findMaxInTree(self, rootNode):
        level = 31
        curNode = rootNode
        max += 1 << rootNode.val
        while curNode.left != None or curNode.right != None:
            curNode = curNode.left if curNode.left != None else curNode.right
            max += 1 << curNode.val

        return max

    def findMaxXorInTree(self, rootNode, arr):
        max = self.findMaxInTree(rootNode)

        level = 31
        curNode = rootNode
        max = 0
        while curNode.left != None or curNode.right != None:
            