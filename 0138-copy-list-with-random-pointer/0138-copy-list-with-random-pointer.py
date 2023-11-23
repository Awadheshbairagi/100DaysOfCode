# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Create a mapping of original nodes to their copies
        mapping = {}

        # First pass: create a shallow copy of each node and store the mapping
        current = head
        while current:
            mapping[current] = Node(current.val)
            current = current.next

        # Second pass: assign next and random pointers in the copied list
        current = head
        while current:
            copy_node = mapping[current]
            copy_node.next = mapping.get(current.next)
            copy_node.random = mapping.get(current.random)
            current = current.next

        return mapping[head]
