class Solution:
    def rob(self, nums: List[int]) -> int:
        # at each house, the max value is robbing it + val from 2 houses ago
        # or not robbing it and taking the value from the last house
        if len(nums) <= 2:
            return max(nums)
        stolen = [nums[0], max(nums[1], nums[0])]

        for i in range(2, len(nums)):
            print(stolen)
            stolen.append(max(nums[i] + stolen[i-2], stolen[i-1]))
            

        print(stolen)
        return stolen[-1]