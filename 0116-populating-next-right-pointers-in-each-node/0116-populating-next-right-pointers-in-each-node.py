class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        # Start from the root and move level by level
        level_start = root
        while level_start.left:
            current = level_start

            # Traverse the current level and set the next pointers
            while current:
                current.left.next = current.right
                if current.next:
                    current.right.next = current.next.left

                # Move to the next node in the same level
                current = current.next

            # Move to the next level
            level_start = level_start.left

        return root
