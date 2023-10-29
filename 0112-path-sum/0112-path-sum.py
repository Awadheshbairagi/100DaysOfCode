# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def check(node, current_sum):
            if not node:
                return False
            current_sum += node.val
            if current_sum == targetSum and not node.left and not node.right:
                return True
            return check(node.left, current_sum) or check(node.right, current_sum)
        
        return check(root, 0)
