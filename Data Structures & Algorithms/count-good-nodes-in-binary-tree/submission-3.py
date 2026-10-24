# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # OK so we need to know the parents first
        # There are miultple paths
        # We need to keep track of the maximum value of the node per path
        
        # Recursion - node, max_val compare and keep going
        # Need to keep track of the count

        good_nodes = 0

        def dfs(node, max_val):
            nonlocal good_nodes
            if not node:
                return 0
            
            if node.val >= max_val:
                good_nodes += 1
                max_val = node.val
            
            dfs(node.left,max_val)
            dfs(node.right, max_val)
    
        dfs(root, float('-inf'))
        return good_nodes