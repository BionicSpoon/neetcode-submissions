class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if bought, can only sell or wait
        # if sold, can only wait (skip the next day)
        # memo[(day, bought)]
        memo = {}
        def rec(day: int, bought: bool) -> int:
            if day >= len(prices):
                return 0
            if (day, bought) in memo:
                return memo[(day, bought)]

            do_nothing = rec(day + 1, bought)
            if bought: # sell or wait
                sell = rec(day + 2, False) + prices[day]
                memo[(day, bought)] = max(sell, do_nothing)
            else:
                buy = rec(day + 1, True) - prices[day]
                memo[(day, bought)] = max(buy, do_nothing)
            return memo[(day, bought)]
        
        return rec(0, False)