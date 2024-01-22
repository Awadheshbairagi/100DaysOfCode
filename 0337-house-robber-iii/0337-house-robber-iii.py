# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root: return [0,0]
            leftpair,rightpair=dfs(root.left),dfs(root.right)
            withroot,without=root.val+leftpair[1]+rightpair[1],max(leftpair)+max(rightpair)
            return [withroot,without]
        return max(dfs(root))