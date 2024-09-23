class Node:
    def __init__(self, val: int = 0):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        if not self.head:
            return -1

        nodeCurr = self.head
        for _ in range(index):
            if (
                not nodeCurr.next
            ):  # check nodeCurr.next to make sure we don't reach nullptr
                return -1
            nodeCurr = nodeCurr.next
        return nodeCurr.val

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
        else:
            nodeCurr = self.head
            while True:
                if not nodeCurr.next:
                    break
                nodeCurr = nodeCurr.next
            nodeCurr.next = newNode
        return

    def addAtIndex(self, index: int, val: int) -> None:
        if not self.head:
            self.head = Node(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            newNode = Node(val)
            currNode = self.head
            for i in range(index):
                if currNode.next == None and i == index - 1:
                    currNode = currNode.next
        return

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        nodeCurr = self.head


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
