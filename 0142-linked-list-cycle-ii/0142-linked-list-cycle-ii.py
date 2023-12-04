class Solution:
    def detectCycle(self, head: ListNode | None, q={}) -> ListNode | None:
        while head:
            if id(head) in q: 
                return head
            q[id(head)] = head
            head = head.next
        return None