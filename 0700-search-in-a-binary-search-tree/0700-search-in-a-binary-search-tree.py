class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def bst(node):
            if not node:
                return None

            if val > node.val:
                return bst(node.right)
            elif val < node.val:
                return bst(node.left)
            else:
                return node
            
            return None

        return bst(root)