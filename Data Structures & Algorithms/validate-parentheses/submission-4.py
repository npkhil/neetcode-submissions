class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            if stack == []:
                return False
            if c == ')':
                if stack[-1] != '(':
                    return False
                stack.pop()
            if c == '}':
                if stack[-1] != '{':
                    return False
                stack.pop()
            if c == ']':
                if stack[-1] != '[':
                    return False
                stack.pop()
        return stack == []
