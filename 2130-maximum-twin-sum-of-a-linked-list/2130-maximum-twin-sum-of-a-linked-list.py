# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res=[]
        while head:
            res.append(head.val)
            head=head.next
        #stored the elements in the array and then traverse parallelly..
        i=0
        j=len(res)-1
        maxi=0
        while(i<j):
            maxi=max(maxi,res[i]+res[j])
            i+=1
            j-=1
        return maxi