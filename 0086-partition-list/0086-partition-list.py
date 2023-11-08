# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode()
        less_tail = less_head
        greater_head = ListNode()
        greater_tail = greater_head
        
        current = head
        
        while current:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next
        
        # Connect the last node of less_head to the first node of greater_head.
        less_tail.next = greater_head.next
        # Set the next of greater_tail to None to avoid cycles in the merged list.
        greater_tail.next = None
        
        # Return the merged list starting from less_head.next.
        return less_head.next
