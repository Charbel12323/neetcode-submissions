# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # return max path sum
        # Path doesnt need to include the root
        # Ok so duplicate nodes
        # Input can never be empty
        # negative numbers

        # Went through a problem
        
        # Each node we have left and right children
        # Therefore to get the maximum path sum for each node
        # We can get the sum of the left children, right children and the current node value

        # So clearly this is going to be post order traversal
        # We would need use dfs
        # 30000
        
        # recursive

        # maximum_sum = float('-inf')
        # FOr each node, we must get the left and right values first

        # node.val + sum_left + sum_right
        # We would compare this value with our current maximum sum
        # and return total_sum
        


        maximum_sum = float('-inf')

        def dfs(node, max_sum):
            nonlocal maximum_sum
            if not node:
                return 0
            
            left_sum = max(0, dfs(node.left, max_sum))
            right_sum = max(0, dfs(node.right, max_sum))

            total_sum = (left_sum + right_sum) + node.val

            maximum_sum = max(maximum_sum, total_sum)

            return node.val + max(left_sum, right_sum)
        
        dfs(root, 0)
        return maximum_sum

        # 