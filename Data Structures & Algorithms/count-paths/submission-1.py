class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        memo = {}
        def rec(i: int, j: int) -> int:
            if i == 1 or j == 1:
                return 1
            
            if (i, j) in memo:
                return memo[(i, j)]
            
            memo[(i, j)] = rec(i-1, j) + rec(i, j-1)
            return memo[(i, j)]

        return rec(m, n)