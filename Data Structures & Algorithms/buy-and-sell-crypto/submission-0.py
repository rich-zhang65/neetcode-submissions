class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 0
        ans = 0

        while left < len(prices):
            right = left + 1
            while right < len(prices) and prices[right] >= prices[left]:
                ans = max(ans, prices[right] - prices[left])
                right += 1

            left = right

        return ans
