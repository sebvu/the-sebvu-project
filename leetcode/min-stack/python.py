class MinStack:

    def __init__(self):
        self.stack = []
        self.setMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.setMin:
            self.setMin.append(val)
        elif val <= self.setMin[-1]:
            self.setMin.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.setMin[-1]:
            self.setMin.pop()

        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.setMin[-1]


minStack = MinStack()

print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-1))
print(minStack.getMin())
print(minStack.top())
print(minStack.pop())
print(minStack.getMin())
