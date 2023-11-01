class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        def inOrderTraversal(node):
            nonlocal prev, count, maxCount, result
            if not node:
                return
            inOrderTraversal(node.left)
            if node.val == prev:
                count += 1
            else:
                count = 1
            if count > maxCount:
                maxCount = count
                result = [node.val]
            elif count == maxCount:
                result.append(node.val)
            prev = node.val
            inOrderTraversal(node.right)        
        prev = None
        count = 1
        maxCount = 0
        result = []
        inOrderTraversal(root)
        return result
