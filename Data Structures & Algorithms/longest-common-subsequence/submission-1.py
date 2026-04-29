class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        # store two pointers (idx) for args for recursive calls
        memo = {}
        def rec(i: int, j: int) -> int:
            if (i, j) in memo:
                return memo[(i, j)]

            if i >= len(s1) or j >= len(s2):
                return 0

            if s1[i] == s2[j]:
                memo[(i, j)] = 1 + rec(i+1, j+1)
                return memo[(i, j)]

            memo[(i, j)] = max(rec(i+1, j), rec(i, j+1))
            return memo[(i, j)]

        return rec(0, 0)