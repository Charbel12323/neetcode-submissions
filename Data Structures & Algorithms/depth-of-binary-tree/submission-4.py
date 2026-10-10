# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # can root be empty, if so would u like me to return 0
        
        # we are going to go as deep down as possible
        # were going to use post order traversal'
        # For every parent, we are either going to get the maximum of the left child or the right child.

        def dfs(node):
            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            return 1 + max(left_height, right_height)
        
        return dfs(root)