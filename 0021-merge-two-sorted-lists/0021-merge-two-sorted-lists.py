# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to simplify the code
        dummy = ListNode(-1)
        current = dummy
        
        # Iterate through both lists and merge them
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # If one of the lists is not empty, append it to the merged list
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        
        # Return the merged list starting from the next of the dummy node
        return dummy.next