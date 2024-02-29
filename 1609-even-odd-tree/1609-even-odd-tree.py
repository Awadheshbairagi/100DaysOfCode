class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        prev = []

        def dfs(current: TreeNode, level: int) -> bool:
            # Base case, an empty tree is Even-Odd
            if current is None:
                return True

            # Compare the parity of current and level
            if current.val % 2 == level % 2:
                return False

            # Add a new level to prev if we've reached a new level
            while(len(prev) <= level):
                prev.append(0)

            # If there are previous nodes on this level, check increasing/decreasing
            # If on an even level, check that current's value is greater than the previous on this level
            # If on an odd level, check that current's value is less than the previous on this level
            if prev[level] != 0 and \
                    ((level % 2 == 0 and current.val <= prev[level]) or \
                     (level % 2 == 1 and current.val >= prev[level])):
                return False

            # Add current value to prev at index level
            prev[level] = current.val

            # Recursively call DFS on the left and right children
            return dfs(current.left, level + 1) and dfs(current.right, level + 1)
        
        current = root
        return dfs(current, 0)
