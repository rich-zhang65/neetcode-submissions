class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        starts = []

        for num in nums:
            if num - 1 not in seen:
                starts.append(num)

        sol = 0
        for s in starts:
            length = 0
            while s in seen:
                length += 1
                sol = max(sol, length)
                s += 1

        return sol
