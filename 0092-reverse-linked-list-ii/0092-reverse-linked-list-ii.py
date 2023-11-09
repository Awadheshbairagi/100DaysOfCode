# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Dummy node to simplify edge cases
        dummy = ListNode(-1)
        dummy.next = head
        prev_left = dummy
        
        # Traverse to the node before left position
        for _ in range(left - 1):
            prev_left = prev_left.next
        
        # Initialize pointers for reversing the sublist
        curr = prev_left.next
        prev = None
        
        # Reverse the sublist from left to right
        for _ in range(right - left + 1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        
        # Connect the reversed sublist back to the original list
        prev_left.next.next = curr
        prev_left.next = prev
        
        return dummy.next
