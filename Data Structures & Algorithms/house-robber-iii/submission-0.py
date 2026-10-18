# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # What is the minimum and maximum number of nodes, 1 - 10000
        # If our input was 2 nodes then we wont be able to rob and return 0
        # And if we have one node then we can just return that value

        # At each node, we can either rob a house or skip a house
        # That means at each node we are going to take 2 different paths
        
        # Naive
        # - For each node, I'd traverse down 2 paths
        # Either skip or rob this house
        # We would need to keep track of the maximum amount of the path and a boolean on whether we can skip or rob
        # return max(of both paths)
        # So since were visiting each node once, the time complexity is going to ben O(h)
        # O(1)

        def dfs(node):
            if not node:
                return(0,0)
            
            left_rob, left_skip = dfs(node.left)
            right_rob, right_skip = dfs(node.right)

            rob = node.val + left_skip + right_skip

            skip = max(left_rob, left_skip) + max(right_rob, right_skip)

            return (rob,skip)
        
        return max(dfs(root))