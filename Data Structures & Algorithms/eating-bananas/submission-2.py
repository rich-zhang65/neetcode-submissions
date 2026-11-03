class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def condition(hours):
            return hours <= h

        left, right = 1, max(piles)
        while left < right:
            mid = left + (right - left) // 2

            hours_to_eat = sum(math.ceil(p / mid) for p in piles)
            if condition(hours_to_eat):
                right = mid
            else:
                left = mid + 1

        return left