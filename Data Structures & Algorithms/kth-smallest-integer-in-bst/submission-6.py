# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Return the kths smallest integer in a BST

        Left side is always smaller
        Right side is always greater
        
        If we do inorder traversal, then we would be return the tree in a sorted order
        In ascending order
        Therefore we can do the traversal and for each node processed, we can keep track of the total nodes processed
        Once it is equal to k we can return it

        K has to be within the number of nodes in the tree
        We can use recursion
        Since we need to process the child first
        Worst case we will be traversing the whole tree which is O(n) where n is the number of nodes

        Space complexity = O(n)
        """

        nodes_processed = 0

        def dfs(node):
            nonlocal nodes_processed

            if not node:
                return None
            
            left = dfs(node.left)
            if left is not None:
                return left

            nodes_processed += 1

            if nodes_processed == k:
                return node.val
            
            right = dfs(node.right)
            if right is not None:
                return right
        
        return dfs(root)