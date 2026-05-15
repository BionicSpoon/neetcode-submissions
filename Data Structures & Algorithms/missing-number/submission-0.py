class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for n in range(len(nums)+1):
            total ^= n
        missing = 0
        for num in nums:
            missing ^= num
        return total ^ missing
