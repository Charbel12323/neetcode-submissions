# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # return 0 if root is empty
        # Is root always a good node - Yes it is
        # Not always guaranteed.
        # were good then

        # Brute force solution - For every node, i'd find its path from root to its current position. Then i'd check if there are any greater values than this current node. If there isnt any then we incremenet the good node count.

        # We can use pre order dfs.
        # To keep track of the roots maximum value we would need to store the maximum value seen so far for this path
        # This allows us to compate the alues whether it is a good node.
        # If any value is greater than the prev_max value then we have to update that as well.

        if not root:
            return 0
        
        good_nodes = 0

        def dfs(node, path_max):
            nonlocal good_nodes

            if not node:
                return
            
            if node.val >= path_max:
                good_nodes += 1
                path_max = node.val
            
            dfs(node.left, path_max)
            dfs(node.right, path_max)
        
        dfs(root, root.val)
        return good_nodes
            




        