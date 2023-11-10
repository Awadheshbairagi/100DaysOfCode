# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # Helper function to find the middle of the linked list
        def find_middle(start, end):
            slow, fast = start, start
            while fast != end and fast.next != end:
                slow = slow.next
                fast = fast.next.next
            return slow

        # Helper function to convert a sorted linked list to BST
        def convert_to_bst(start, end):
            if start == end:
                return None

            mid = find_middle(start, end)
            root = TreeNode(mid.val)
            root.left = convert_to_bst(start, mid)
            root.right = convert_to_bst(mid.next, end)
            return root

        return convert_to_bst(head, None)
