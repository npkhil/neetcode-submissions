class MinStack:

    def __init__(self):
        self.stack = []
        self.minElement = math.inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minElement:
            self.minElement = val

    def pop(self) -> None:
        val = self.stack.pop()
        if not self.stack:
            self.minElement = math.inf
            return
        if val == self.minElement: 
            self.minElement = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minElement
