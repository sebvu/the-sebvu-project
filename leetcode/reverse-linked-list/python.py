# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # recursive solution
        if head is None or head.next is None:
            return

        curr = head
        prev = None

        while curr.next is not None:
            head = curr.next  # set head to the next node
            curr.next = prev  # set curr.next to prev node,
            prev = curr  # set a new prev
            curr = head  # iterate the curr up by one
        curr.next = prev

        return head


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative solution
        if head is None or head.next is None:
            return

        curr = head
        prev = None

        while curr.next is not None:
            head = curr.next  # set head to the next node
            curr.next = prev  # set curr.next to prev node,
            prev = curr  # set a new prev
            curr = head  # iterate the curr up by one

        return head
