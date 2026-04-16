class Solution:
    def climbStairs(self, n: int) -> int:
        # ways[step=n] = ways[n-1] + ways[n-2]
        ways = [0] * (n + 1)

        for i in range(len(ways)):
            if i == 0 or i == 1:
                ways[i] = 1
                continue
            ways[i] = ways[i-1] + ways[i-2]

        return ways[n]
