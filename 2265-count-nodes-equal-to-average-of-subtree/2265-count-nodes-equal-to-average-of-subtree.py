class Solution:
    def __init__(self):
        self.count = 0
    def postOrder(self, root: TreeNode) -> Tuple[int, int]:
        if not root:
            return 0, 0
        left_sum, left_count = self.postOrder(root.left)
        right_sum, right_count = self.postOrder(root.right)
        node_sum = left_sum + right_sum + root.val
        node_count = left_count + right_count + 1
        if root.val == node_sum // node_count:
            self.count += 1
        return node_sum, node_count
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.postOrder(root)
        return self.count
