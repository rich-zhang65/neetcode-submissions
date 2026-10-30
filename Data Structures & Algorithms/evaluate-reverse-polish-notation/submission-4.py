import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        def trunc_div(a, b):
            exact_res = a / b
            floor_res = a // b
            return floor_res if exact_res == floor_res or floor_res >= 0 else floor_res + 1

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
        