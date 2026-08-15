class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+' : lambda a, b: a + b, '-' : lambda a, b: a - b, '*' : lambda a, b: a * b, '/' : lambda a, b: a // b + 1 if a / b < 0 and a / b != float(a // b) else a // b}
        stack = []
        for t in tokens:
            # print(t)
            if t not in operators.keys():
                stack.append(int(t))
            else:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[t](a,b))
            # print(stack)
        return stack[-1]