class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # memo[(idx, subtotal)]: ways to reach target
        memo = {}
        def rec(i: int, subtotal: int) -> int:
            if i >= len(nums):
                return 0
            if (i, subtotal) in memo:
                return memo[(i, subtotal)]
            ways = 0
            if i == len(nums) - 1:
                if nums[i] + subtotal == target:
                    ways += 1
                if -nums[i] + subtotal == target:
                    ways += 1
                return ways

            ways += rec(i + 1, subtotal + nums[i])
            ways += rec(i + 1, subtotal - nums[i])
            memo[(i, subtotal)] = ways
            return ways
        
        return rec(0, 0)