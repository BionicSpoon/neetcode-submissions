class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        res = []

        for i in range(len(nums)):
            if nums[i] in complements:
                return [complements[nums[i]], i]
            else:
                complements[target - nums[i]] = i
