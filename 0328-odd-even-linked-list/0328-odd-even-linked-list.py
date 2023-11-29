# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if(head==None or head.next==None):
            return head
        th1=h1=head
        th2=h2=head.next
        th=h2.next
        i=1
        while(th!=None):
            if(i%2==0):
                th2.next=th
                th2=th
            else:
                th1.next=th
                th1=th
            th=th.next
            i+=1
        th2.next=None
        th1.next=None
        th1.next=h2
        return h1