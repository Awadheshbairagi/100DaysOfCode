# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        
        # Previous pointer to keep track of the previous node
        prev = dummy
        
        while head:
            # If the current node and the next node have the same value
            if head.next and head.val == head.next.val:
                # Skip nodes with duplicate values
                while head.next and head.val == head.next.val:
                    head = head.next
                # Remove nodes with duplicate values
                prev.next = head.next
            else:
                # Move the previous pointer and current pointer to the next nodes
                prev = prev.next
            head = head.next
        
        # Return the sorted and distinct linked list
        return dummy.next
