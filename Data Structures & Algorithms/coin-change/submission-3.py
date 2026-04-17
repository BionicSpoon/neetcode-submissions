class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Approach 1 - bottom up with array cache for each amount up to target
        
        # recursive: min_coins[n] = min(min_coins[n-c] for c in coins) + 1
        # semi-brute force?
        # maybe good enough?

        min_coins = [0]
        for tgt in range(1, amount+1):
            #print(tgt, min_coins)
            # coin_found = False
            # for c in coins:
            #     if c == tgt:
            #         #print(c)
            #         min_coins.append(1)
            #         #print(min_coins)
            #         coin_found = True
            #         break
            # if coin_found:
            #     continue
            cur_min_coins = math.inf
            for c in coins:
                if tgt - c >= 0 and min_coins[tgt-c] >= 0:
                    cur_min_coins = min(cur_min_coins, min_coins[tgt-c] + 1)
            min_coins.append(cur_min_coins if cur_min_coins != math.inf else -1)
            #print(min_coins)

        return min_coins[-1] if min_coins[-1] != math.inf else -1