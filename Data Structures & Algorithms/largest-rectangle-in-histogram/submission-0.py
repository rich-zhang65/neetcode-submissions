class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(heights) + 1):
            while stack and (i == len(heights) or heights[i] <= heights[stack[-1]]):
                top_idx = stack.pop()
                width = (i - 1) - stack[-1] if stack else i
                ans = max(ans, width * heights[top_idx])

            stack.append(i)
        
        return ans
