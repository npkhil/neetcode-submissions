class MinStack:

    def __init__(self):
        self.stack = []
        self.preMin = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.preMin:
            self.preMin.append(min(val, self.preMin[-1]))
        else:
            self.preMin.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.preMin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.preMin[-1]
