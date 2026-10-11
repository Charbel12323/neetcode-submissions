# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # [1,2,3,4] - preorder
        # [2,1,3,4] - inorder

        # node - > left -> right
        # left -> node -> right

        # 1 -> 2 -> 3 -> 4

        # pre order gives us the root value. Then we can use inorder to figure out the left and right tree

        # Every parent has one left child and one right child

        # If im going to look up the root in the inorder array thats going to be O(n)
        # I need to find a way to get the index of the root using preorder array
        # Hashmap - I can store all the values with there corresponding index in the hashmap
        # once we get that index we know, i could figure out whats on the left tree and whats on the right tree
        # once we do that we can get the next root value and do the same thing recursively

        inorder_index = {} # value -> i

        for i, value in enumerate(inorder):
            inorder_index[value] = i
        
        preorder_index = 0
        
        
        
        def dfs(left, right):
            nonlocal preorder_index
            
            if left > right:
                return None

            idx_inorder = inorder_index[preorder[preorder_index]]
            preorder_index += 1

            root_value = inorder[idx_inorder]

            node = TreeNode(root_value)

            node.left = dfs(left, idx_inorder - 1)
            node.right = dfs(idx_inorder + 1, right)

            return node
        
        return dfs(0, len(inorder) - 1)
            


