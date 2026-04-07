class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        prefixes = [1] * len(nums)
        suffixes = [1] * len(nums)
        product = 1
        for i in range(len(nums)-1):
            product *= nums[i]
            prefixes[i] = product

        product = 1
        for i in range(len(nums)-1, 0, -1):
            product *= nums[i]
            suffixes[i] = product

        for i in range(len(nums)):
            res.append((prefixes[i-1] if i > 0 else 1) * (suffixes[i+1] if i+1 < len(nums) else 1))

        return res