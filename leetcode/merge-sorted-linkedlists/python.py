# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        mergeListCurr = ListNode()
        mergeListHead = mergeListCurr

        while list1 and list2:
            mergeListCurr.next = ListNode()
            if list1.val <= list2.val:
                newNode = ListNode(list1.val)
                mergeListCurr = newNode
                mergeListCurr = mergeListCurr.next
                list1 = list1.next
            else:
                newNode = ListNode(list2.val)
                mergeListCurr = newNode
                mergeListCurr = mergeListCurr.next
                list2 = list2.next

        if not list1:
            while list2:
                newNode = ListNode(list2.val)
                mergeListCurr = newNode
                mergeListCurr = mergeListCurr.next
                list2 = list2.next
        else:
            while list1:
                newNode = ListNode(list1.val)
                mergeListCurr = newNode
                mergeListCurr = mergeListCurr.next
                list1 = list1.next
        return mergeListHead
