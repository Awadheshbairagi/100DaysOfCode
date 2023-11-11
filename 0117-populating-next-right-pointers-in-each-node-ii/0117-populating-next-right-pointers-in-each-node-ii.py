class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        level_start = root

        while level_start:
            current = level_start
            while current:
                if current.left:
                    if current.right:
                        current.left.next = current.right
                    else:
                        current.left.next = self.findNext(current.next)
                if current.right:
                    current.right.next = self.findNext(current.next)

                current = current.next

            level_start = self.findNext(level_start)

        return root

    def findNext(self, node: 'Node') -> 'Node':
        while node:
            if node.left:
                return node.left
            if node.right:
                return node.right
            node = node.next
        return None
