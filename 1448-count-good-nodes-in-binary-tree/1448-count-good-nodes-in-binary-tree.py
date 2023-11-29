# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = []

        def dfs(node, prev_max=float("-inf")):
            if not node:
                return None
            nonlocal res

            if prev_max<=node.val:
                res.append(node.val)

            prev_max = max(node.val, prev_max)

            if node.left:
                dfs(node.left, prev_max)
            
            if node.right:
                dfs(node.right, prev_max)
        
        dfs(root)
        return len(res)
        

