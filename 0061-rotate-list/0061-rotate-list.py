# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base cases
        if not head or not head.next or k == 0:
            return head
        
        # Calculate the length of the linked list
        length = 1
        current = head
        while current.next:
            length += 1
            current = current.next
        
        # Calculate the new head position after rotation
        k %= length
        if k == 0:
            return head
        
        # Find the new tail and update pointers
        current = head
        for _ in range(length - k - 1):
            current = current.next
        
        new_head = current.next
        current.next = None
        
        # Update the tail's next pointer to the original head
        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = head
        
        return new_head
