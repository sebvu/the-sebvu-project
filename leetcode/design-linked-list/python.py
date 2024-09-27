class Node:
    def __init__(self, var, prev=None, next=None):
        self.val = var
        self.next = next
        self.prev = prev


class MyLinkedList:

    def __init__(self):  # dummy nodes
        self.left = Node(0)
        self.right = Node(0)
        self.left.next = self.right
        self.right.prev = self.left

    def get(self, index: int) -> int:
        curr, count = self.left.next, 0
        while curr != self.right and count < index:
            curr = curr.next
            count += 1
        if curr == self.right:
            return -1
        return curr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val, self.left, self.left.next)
        self.left.next.prev = newNode
        self.left.next = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val, self.right.prev, self.right)
        self.right.prev.next = newNode
        self.right.prev = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        curr, count = self.left.next, 0
        while curr != self.right and count < index:
            curr = curr.next
            count += 1
        if curr == self.right:
            if index == 0 or index == count:
                newNode = Node(val, self.right.prev, self.right)
                self.right.prev.next = newNode
                self.right.prev = newNode
            return
        else:
            newNode = Node(val, curr.prev, curr)
            curr.prev.next = newNode
            curr.prev = newNode

    def deleteAtIndex(self, index: int) -> None:
        curr, count = self.left.next, 0
        while curr != self.right and count < index:
            curr = curr.next
            count += 1
        if curr == self.right:
            return
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
            del curr


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
