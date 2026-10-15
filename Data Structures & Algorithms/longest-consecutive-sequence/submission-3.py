class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        seen = defaultdict(int)
        sol = 0

        for num in num_set:
            length = seen[num - 1] + seen[num + 1] + 1
            seen[num - seen[num - 1]] = length
            seen[num + seen[num + 1]] = length
            sol = max(sol, length)

        return sol
