# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Helper function to reverse a linked list
        def reverseList(node):
            prev, curr = None, node
            while curr:
                next_temp = curr.next
                curr.next = prev
                prev = curr
                curr = next_temp
            return prev
        
        # Find the midpoint of the linked list
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        second_half = reverseList(slow)
        
        # Compare the first half and reversed second half
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        
        return True
