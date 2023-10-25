# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0, True
            
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            
            # If either subtree is not balanced, the entire tree is not balanced
            if not left_balanced or not right_balanced:
                return 0, False
            
            # If the height difference between left and right subtree is more than 1, the tree is not balanced
            if abs(left_height - right_height) > 1:
                return 0, False
            
            # Return the height of the current node's subtree and whether it's balanced
            return max(left_height, right_height) + 1, True
        
        _, balanced = check_balance(root)
        return balanced
