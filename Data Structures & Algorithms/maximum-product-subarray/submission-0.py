class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_pos = [x for x in nums]
        max_neg = [x for x in nums]

        for i in range(1, len(nums)):
            max_pos[i] = max(max_pos[i-1] * nums[i], nums[i], max_neg[i-1] * nums[i])
            max_neg[i] = min(max_pos[i-1] * nums[i], nums[i], max_neg[i-1] * nums[i])

        return max(max_pos)