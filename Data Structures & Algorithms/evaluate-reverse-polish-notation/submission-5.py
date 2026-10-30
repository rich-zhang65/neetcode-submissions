import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def trunc_div(a, b):
            return int(a / b)

        arithmetic_map = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': trunc_div,
        }

        for t in tokens:
            if t in arithmetic_map:
                right = stack.pop()
                left = stack.pop()
                stack.append(arithmetic_map[t](left, right))
            else:
                stack.append(int(t))

        return stack[0]
        