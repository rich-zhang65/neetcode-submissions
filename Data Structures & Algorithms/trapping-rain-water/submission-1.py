class Solution:
    def trap(self, height: List[int]) -> int:
        prefixes = []
        suffixes = []

        max_prefix, max_suffix = 0, 0
        for i in range(len(height)):
            prefixes.append(max_prefix)
            suffixes.append(max_suffix)

            max_prefix = max(height[i], max_prefix)
            max_suffix = max(height[len(height) - 1 - i], max_suffix)

        suffixes.reverse()
        
        ans = 0
        for i, h in enumerate(height):
            ans += max(0, min(prefixes[i], suffixes[i]) - h)

        return ans
