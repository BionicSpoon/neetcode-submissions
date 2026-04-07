class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        low = prices[0]
        for price in prices:
            low = min(low, price)
            best = max(best, price - low)
        return best
