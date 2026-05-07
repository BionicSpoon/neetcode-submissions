class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # at each letter, either take it or skip it
        # -> only two recursive calls?
        # memo[(si, ti)]: int
        # meaning: how many ways are there to get s[si:] from t[ti:] ?


        memo = {}
        def rec(si: int, ti: int) -> int:
            if ti == len(t): # prev version returned early D:
                return 1
            if si >= len(s):
                return 0

            if (si, ti) in memo:
                return memo[(si, ti)]

            take = 0
            if s[si] == t[ti]:
                take = rec(si + 1, ti + 1)
            skip = rec(si + 1, ti)
            res = take + skip
            memo[(si, ti)] = res
            return res

        res = rec(0, 0)
        return res