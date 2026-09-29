"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        old_to_new = {} # oldNode -> newNode

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            
            copiedNode = Node(node.val)

            old_to_new[node] = copiedNode

            for nieghbor in node.neighbors:
                copiedNeighbor = dfs(nieghbor)
                copiedNode.neighbors.append(copiedNeighbor)
        
            return copiedNode
        
        return dfs(node)