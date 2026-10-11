# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # left is smaller , right is larger.
        # from root when we go left, the max value will always be root
        # from root when go right, the min value will always be root
        # So on the left side we must always update the max value
        # on the right side we shoudl awlways update the min value

        def dfs(node, max_value, min_value):
            if not node:
                return True
            
            if node.val >= max_value or node.val <= min_value:
                return False
            
            return dfs(node.left, node.val, min_value) and dfs(node.right, max_value,node.val )
        
        return dfs(root, float('inf'), float('-inf'))
            

