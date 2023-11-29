# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, ll: Optional[ListNode]) -> Optional[ListNode]:
        def CreateList(args):
            if not args:
                return None
            head = ListNode(args[0])
            current = head
            for x in args[1:]:
                node = ListNode(x)
                current.next = node
                current = current.next
            return head
        p = []
        while ll:
            p.append(ll.val)
            ll = ll.next
        return CreateList(p[::-1])