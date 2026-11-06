class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        min_to_buy = prices[0]

        for p in prices:
            ans = max(ans, p - min_to_buy)
            min_to_buy = min(min_to_buy, p)

        return ans
        