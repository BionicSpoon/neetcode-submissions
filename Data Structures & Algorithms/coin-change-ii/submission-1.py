class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort(reverse=True)
        memo = {}

        def rec(subtotal: int, i: int) -> int:
            if (subtotal, i) in memo:
                return memo[(subtotal, i)]
            if subtotal == amount:
                return 1
            if subtotal > amount or i >= len(coins):
                return 0
            

            res = 0
            res += rec(subtotal + coins[i], i) # take the current
            res += rec(subtotal, i+1) # skip it

            memo[(subtotal, i)] = res
            return res

        return rec(0, 0)
