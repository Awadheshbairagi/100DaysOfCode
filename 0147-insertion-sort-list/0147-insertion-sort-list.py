# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to serve as the head of the sorted list
        dummy = ListNode(0)
        current = head
        
        while current:
            # Store the next node to be considered
            next_node = current.next
            # Find the correct position to insert the current node in the sorted list
            sorted_node = dummy
            while sorted_node.next and sorted_node.next.val < current.val:
                sorted_node = sorted_node.next
            
            # Insert the current node in the sorted list
            current.next = sorted_node.next
            sorted_node.next = current
            
            # Move to the next node in the original list
            current = next_node
        
        return dummy.next
