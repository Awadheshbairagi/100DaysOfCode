# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy head of the result list
        dummy_head = ListNode(0)
        current = dummy_head  # Pointer to the current node in the result list
        carry = 0  # Initialize the carry to 0
        
        # Traverse both input lists
        while l1 or l2:
            # Get the values at the current nodes (if available)
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            
            # Calculate the sum of the current nodes and the carry
            total = l1_val + l2_val + carry
            carry = total // 10  # Update the carry
            
            # Create a new node with the units digit of the total
            current.next = ListNode(total % 10)
            current = current.next  # Move the pointer forward
            
            # Move to the next nodes in the input lists (if available)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # If there's a carry after processing all nodes, create an additional node
        if carry > 0:
            current.next = ListNode(carry)
        
        # The result list starts from the next node of the dummy head
        return dummy_head.next
