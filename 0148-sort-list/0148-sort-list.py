class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # Find the middle of the linked list
        middle = self.find_middle(head)

        # Split the linked list into two halves
        left_half = head
        right_half = middle.next
        middle.next = None

        # Recursively sort the two halves
        left_sorted = self.sortList(left_half)
        right_sorted = self.sortList(right_half)

        # Merge the sorted halves
        return self.merge(left_sorted, right_sorted)

    def find_middle(self, head):
        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, left, right):
        dummy = ListNode()
        current = dummy

        while left and right:
            if left.val < right.val:
                current.next = left
                left = left.next
            else:
                current.next = right
                right = right.next

            current = current.next

        # Append the remaining nodes from either list
        if left:
            current.next = left
        elif right:
            current.next = right

        return dummy.next
