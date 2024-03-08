class Solution:
    def middleNode(self, h: Optional[ListNode]) -> Optional[ListNode]:
        return (f:=h) and all(f and f.next and (h:=h.next,f:=f.next.next) for _ in count()) or h