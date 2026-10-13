class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = [[] for _ in range(len(nums) + 1)]

        count_map = defaultdict(int)
        for num in nums:
            count_map[num] += 1

        for key, val in count_map.items():
            freqs[val].append(key)

        sol = []
        for i in range(len(freqs) - 1, -1, -1):
            for num in freqs[i]:
                sol.append(num)

                if len(sol) == k:
                    return sol