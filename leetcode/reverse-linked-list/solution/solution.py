# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # recursive solution
#         if not head:
#             return None
#
#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None
#
#         return newHead


# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # iterative solution
#
#         curr, prev = head, None
#
#         while curr:
#             head = curr.next  # set head to the next node
#             curr.next = prev  # set curr.next to prev node,
#             prev = curr  # set a new prev
#             curr = head  # iterate the curr up by one
#         return prev
