class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        low = prices[0]
        for i, price in enumerate(prices):
            if i == 0:
                continue
            low = min(low, price)
            best = max(best, price - low)
        return best
