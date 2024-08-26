class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # evaluate the minimum value between val and last value of minStack, if no minStack then just val
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # omit the check of comparing
        # if self.stack[-1] == self.setMin[-1]:
        # as it is not needed
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


minStack = MinStack()

print(minStack.push(-2))
print(minStack.push(0))
print(minStack.push(-1))
print(minStack.getMin())
print(minStack.top())
print(minStack.pop())
print(minStack.getMin())
