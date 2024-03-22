# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head.next == None:
            return True 
        slow, fast, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        center    = slow    
        prev.next = None  
        prev, current = None, center
        while(current):
            following    = current.next
            current.next = prev
            prev         = current
            current      = following
        inversed = prev    
        while head:
            if head.val!=inversed.val:
                return False
            head     = head.next
            inversed = inversed.next
        return True