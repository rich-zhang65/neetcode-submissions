class Solution:
    def trap(self, height: List[int]) -> int:
        left_wall, right_wall = 0, len(height) - 1
        
        ans = 0
        left_max, right_max = height[left_wall], height[right_wall]
        while left_wall < right_wall:
            if height[left_wall] < height[right_wall]:
                left_wall += 1
                left_max = max(left_max, height[left_wall])
                ans += left_max - height[left_wall]
            else:
                right_wall -= 1
                right_max = max(right_max, height[right_wall])
                ans += right_max - height[right_wall]
        
        return ans