class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0, True
            
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            
            if not left_balanced or not right_balanced:
                return 0, False
            if abs(left_height - right_height) > 1:
                return 0, False
            return max(left_height, right_height) + 1, True
        
        _, balanced = check_balance(root)
        return balanced
