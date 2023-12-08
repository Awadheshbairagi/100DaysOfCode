# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        ans=[]
        def preorder(root):
            if not root:
                return
            ans.append("(")
            ans.append(str(root.val))
            if not root.left and root.right:
                ans.append("()")
            preorder(root.left)
            preorder(root.right)
            ans.append(")")
        preorder(root)            
        return "".join(ans)[1:-1]