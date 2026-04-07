class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            next_num = nums[(mid + 1) % len(nums)]
            if nums[mid] > next_num:
                return next_num

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

                
        return nums[0] # this means nums is one element ig