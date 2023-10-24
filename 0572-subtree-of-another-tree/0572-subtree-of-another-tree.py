# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isMatch(node1, node2):
            if not node1 and not node2:
                return True
            if not node1 or not node2:
                return False
            return node1.val == node2.val and isMatch(node1.left, node2.left) and isMatch(node1.right, node2.right)
        
        def dfs(node):
            if not node:
                return False
            if isMatch(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)
        
        return dfs(root)
