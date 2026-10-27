class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing_braces = {
            ')': '(',
            '}': '{',
            ']': '[',
        }

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
                continue
            
            if len(stack) == 0:
                return False

            top = stack.pop()
            if closing_braces[ch] != top:
                return False
            
        return len(stack) == 0