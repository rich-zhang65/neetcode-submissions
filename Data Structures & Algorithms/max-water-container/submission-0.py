class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ptr1, ptr2 = 0, len(heights) - 1

        ans = 0
        while ptr1 < ptr2:
            height1 = heights[ptr1]
            height2 = heights[ptr2]

            ans = max(ans, min(height1, height2) * (ptr2 - ptr1))

            if height1 < height2:
                ptr1 += 1
            else:
                ptr2 -= 1
        
        return ans
