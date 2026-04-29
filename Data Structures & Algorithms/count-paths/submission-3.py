class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        for i in range(m+1):
            dp[(i, 0)] = 1
        for j in range(n+1):
            dp[(0, j)] = 1

        for i in range(1, m):
            for j in range(1, n):
                dp[(i, j)] = dp[(i-1, j)] + dp[(i, j-1)]

        return dp[(m-1, n-1)]


        # memo = {}
        # def rec(i: int, j: int) -> int:
        #     if i == 1 or j == 1:
        #         return 1
            
        #     if (i, j) in memo:
        #         return memo[(i, j)]
            
        #     memo[(i, j)] = rec(i-1, j) + rec(i, j-1)
        #     return memo[(i, j)]

        # return rec(m, n)