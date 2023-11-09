# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.first_node = None
        self.second_node = None
        self.prev_node = TreeNode(float('-inf'))
        
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Helper function to perform in-order traversal and find swapped nodes
        def inorder_traversal(node):
            if not node:
                return
            # Traverse left subtree
            inorder_traversal(node.left)
            
            # Check if current node's value is smaller than the previous node's value
            if node.val <= self.prev_node.val:
                if not self.first_node:
                    self.first_node = self.prev_node  # First swapped node found
                self.second_node = node  # Second swapped node found
            
            self.prev_node = node  # Update previous node
            
            # Traverse right subtree
            inorder_traversal(node.right)
        
        # Perform in-order traversal to find the swapped nodes
        inorder_traversal(root)
        
        # Swap the values of the two nodes to recover the BST
        self.first_node.val, self.second_node.val = self.second_node.val, self.first_node.val
