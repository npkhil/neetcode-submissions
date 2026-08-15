class MinStack:

    def __init__(self):
        self.stack = []
        self.minval = math.inf

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minval = val
        else:
            self.stack.append(val - self.minval)
            if val < self.minval:
                self.minval = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val < 0:
            self.minval -= val

    def top(self) -> int:
        val = self.stack[-1]
        if val < 0:
            return self.minval
        else:
            return val + self.minval

    def getMin(self) -> int:
        return self.minval
        
