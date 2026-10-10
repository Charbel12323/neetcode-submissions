# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # longest path between any two nodes
        # Doesn;t need to pass through root
        # Can;t include same node twice
        # Return the diamater

        # per parent node
        # How is the diamater calculated
        # its left height + right_height + 1 ( current parent )
        # post order traversal
        # Were going to get the left height first, then the right height
        # and then return whats mentioned above
        if not root:
            return 0
        
        maximum_diameter = 0

        def dfs(node):
            nonlocal maximum_diameter

            if not node:
                return 0
            
            left_height = dfs(node.left)
            right_height = dfs(node.right)

            maximum_diameter = max(maximum_diameter, left_height + right_height)


            return 1 + max(left_height, right_height)
        
        dfs(root)
        return maximum_diameter