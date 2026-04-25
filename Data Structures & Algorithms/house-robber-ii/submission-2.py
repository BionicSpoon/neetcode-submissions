class Solution:
    def rob(self, nums: List[int]) -> int:
        # fundamentally the same as House Robber I, just first and last house are connected.
        # -> Either ignore first or last house
        # and run House Robber I on each possibility
        if len(nums) <= 2:
            return max(nums)

        first = nums[0]
        nums = nums[1:]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        # check dp[i-2] + nums[i] vs dp[i-1]

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        rob1 = dp[-1]

        nums = [first] + nums[:-1]
        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        return max(rob1, dp[-1])