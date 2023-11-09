# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inorder_traversal(node, result):
            if not node:
                return
            inorder_traversal(node.left, result)
            result.append(node.val)
            inorder_traversal(node.right, result)
        
        # Perform in-order traversal to get the elements
        elements = []
        inorder_traversal(root, elements)
        
        # Check if the elements are sorted in ascending order
        for i in range(1, len(elements)):
            if elements[i] <= elements[i - 1]:
                return False
        
        return True
