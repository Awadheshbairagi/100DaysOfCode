# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: if both nodes are None, they are equal
        if not p and not q:
            return True
        # If one node is None while the other is not, they are not equal
        if not p or not q:
            return False
        # Check if the values are equal and recursively check left and right subtrees
        return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
