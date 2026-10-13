class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)
        sol = []

        for num in nums:
            counts[num] -= 1

        pq = list(map(lambda x: x[::-1], counts.items()))
        heapq.heapify(pq)
        
        for i in range(k):
            _, val = heapq.heappop(pq)
            sol.append(val)

        return sol