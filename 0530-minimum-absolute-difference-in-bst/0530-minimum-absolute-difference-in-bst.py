class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        def inOrderTraversal(node):
            nonlocal prev_val, min_diff
            
            if not node:
                return
            
            inOrderTraversal(node.left)
            
            if prev_val is not None:
                min_diff = min(min_diff, node.val - prev_val)
            
            prev_val = node.val
            
            inOrderTraversal(node.right)
        
        prev_val = None
        min_diff = float('inf')
        
        inOrderTraversal(root)
        
        return min_diff
