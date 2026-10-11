# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # can k > len(input)
        # is there always a guarenteed solution
        # can k = 0

        # BST if we do inorder traversal on the BST we would end up getting a sorted array.
        # we can store the results in an array until the len(array) == k: 
        # space = O(h)

        results = []

        def dfs(node):
            nonlocal results

            if not node:
                return
            
            dfs(node.left)

            if len(results) == k:
                return

            results.append(node.val)

            dfs(node.right)
        
        dfs(root)
        
        return results[-1]
