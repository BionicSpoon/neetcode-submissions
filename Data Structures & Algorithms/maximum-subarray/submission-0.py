class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = -math.inf
        max_sum = cur_sum
        for num in nums:
            cur_sum += num
            cur_sum = max(cur_sum, num)
            max_sum = max(cur_sum, max_sum)
            
        return max_sum