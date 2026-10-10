# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # inorder traversal
        # we are going to compare
        # if they are equal keep going
        
        def dfs(nodeP, nodeQ):
            if not nodeP and not nodeQ:
                return True
            
            if not nodeP or not nodeQ:
                return False
            
            if (nodeP.val != nodeQ.val):
                return False
            
            return dfs(nodeP.left, nodeQ.left) and dfs(nodeP.right, nodeQ.right)
        
        return dfs(p, q)

