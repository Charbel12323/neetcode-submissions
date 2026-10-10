# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # inorder dfs.
        # Why inorder. Is once we find a matching. node, then we check if left and right are working.
        # Why dfs. I chose dfs cause once we find a matching node its very easy to check if the left and right are the same
        # We are going to compare each value in node with the current root of value of subroot
        # if they match then we can keep diving deeper, if they dont match we are going to keep traversig left and right
        # isSameTree(node, subroot) -> This check whether the tree is the same
        # if it is we keep going
        # return isSameTree

        if not root:
            return False
        
        if root.val == subRoot.val:
            if self.isSameTree(root, subRoot):
                return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    def isSameTree(self, node, subRoot):
        if not node and not subRoot:
            return True
        
        if not node or not subRoot:
            return False
        
        if node.val != subRoot.val:
            return False
        
        return self.isSameTree(node.left, subRoot.left) and self.isSameTree(node.right, subRoot.right)
    