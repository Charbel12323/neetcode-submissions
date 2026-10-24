# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        count = 0
        smallest_value = None

        def dfs(node):
            nonlocal count, smallest_value
            if not node:
                return None
            
            dfs(node.left)

            if smallest_value is not None:
                return
            
            count += 1

            if count == k:
                smallest_value = node.val
            
            dfs(node.right)
        
        dfs(root)
        return smallest_value
            
        