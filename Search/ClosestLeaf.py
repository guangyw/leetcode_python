# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution:
    def findClosestLeaf(self, root, k):
        graph = defaultdict(list)
        leaves = set()
        visited = set()
        start = []
        
        def buildGraph(node, parent, k):
            if not node: return
       
            if node.val == k:
                start.append(node)
                
            if not node.left and not node.right:
                leaves.add(node)
                        
            if parent:
                graph[node].append(parent)
                graph[parent].append(node)
            
            buildGraph(node.left, node, k)
            buildGraph(node.right, node, k)
        
        buildGraph(root, None, k)
        
        q = deque([start])
        
        while q:
            size = len(q)
            for _ in range(size):
                node = q.popleft()
                if node in visited:
                    continue
                
                visited.add(node)
                
                if node in leaves:
                    return node.val
                
                for neighbor in graph[node]:
                    q.append(neighbor)
                
        
        return None