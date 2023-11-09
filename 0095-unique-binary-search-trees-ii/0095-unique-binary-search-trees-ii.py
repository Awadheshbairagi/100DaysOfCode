# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate_trees_helper(start, end):
            trees = []
            if start > end:
                trees.append(None)
                return trees
            
            for root_val in range(start, end + 1):
                left_subtrees = generate_trees_helper(start, root_val - 1)
                right_subtrees = generate_trees_helper(root_val + 1, end)
                
                for left_tree in left_subtrees:
                    for right_tree in right_subtrees:
                        root = TreeNode(root_val)
                        root.left = left_tree
                        root.right = right_tree
                        trees.append(root)
            return trees
        
        if n == 0:
            return []
        return generate_trees_helper(1, n)
