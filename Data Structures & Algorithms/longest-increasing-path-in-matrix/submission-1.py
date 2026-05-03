class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # brute force: expand from all tiles to all adj tiles > it
        # slightly less brute force: only expand from tiles with no adj smaller value
        # as we expand, when we find a longest increasing path starting somewhere,
        # we can cache memo[(i, j)] = longest path starting from (i, j)
        # then, if a neighbor is in memo and we are on a tile < neighbor, we can
        # consider all memos and basic expansions, and take the longest for this value
        # then cache it, rinse and repeat
        memo = {}
        def rec(i: int, j: int, prev: int) -> int:
            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0
            cur = matrix[i][j]
            if cur <= prev:
                return 0
            if (i, j) in memo:
                return memo[(i, j)]

            longest = max(rec(i-1, j, cur), rec(i+1, j, cur))
            longest = max(longest, rec(i, j-1, cur), rec(i, j+1, cur))
            memo[(i, j)] = longest + 1
            return memo[(i, j)]

        longest = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                longest = max(longest, rec(i, j, -math.inf))

        return longest
