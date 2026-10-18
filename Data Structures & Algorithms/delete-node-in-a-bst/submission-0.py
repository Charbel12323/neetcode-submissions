class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        parent = None
        node = root

        # Step 1: Find the node and its parent
        while node and node.val != key:
            parent = node

            if key < node.val:
                node = node.left
            else:
                node = node.right

        # Key not found
        if not node:
            return root

        # Step 2: If node has two children
        if node.left and node.right:
            successor_parent = node
            successor = node.right

            # Find smallest node in right subtree
            while successor.left:
                successor_parent = successor
                successor = successor.left

            # Replace value of target node
            node.val = successor.val

            # Now delete the successor instead
            parent = successor_parent
            node = successor

        # Step 3: Node now has at most one child
        child = node.left if node.left else node.right

        # If deleting root
        if parent is None:
            return child

        # Update parent's pointer
        if parent.left is node:
            parent.left = child
        else:
            parent.right = child

        return root