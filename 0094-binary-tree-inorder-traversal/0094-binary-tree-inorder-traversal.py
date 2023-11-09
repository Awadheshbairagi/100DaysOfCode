# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Traverse left subtree and push nodes onto the stack
            while current:
                stack.append(current)
                current = current.left
            
            # Pop a node from the stack and add its value to the result
            current = stack.pop()
            result.append(current.val)
            
            # Move to the right subtree
            current = current.right
        
        return result
