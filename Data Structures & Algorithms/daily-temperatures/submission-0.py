class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []

        for idx, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                top = stack.pop()
                ans[top] = idx - top

            stack.append(idx)

        return ans
        