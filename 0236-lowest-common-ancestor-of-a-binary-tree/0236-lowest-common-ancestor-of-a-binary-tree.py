class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base case: if the root is None or matches any of the target nodes, return the root
        if not root or root == p or root == q:
            return root
        
        # Search left and right subtrees
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # If both p and q are found in different subtrees, root is the LCA
        if left and right:
            return root
        
        # If only one node is found, return that node (ancestor)
        return left if left else right
