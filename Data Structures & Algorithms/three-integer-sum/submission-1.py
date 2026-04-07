class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        prev_i = None

        for i in range(len(nums)):
            if nums[i] == prev_i:
                continue
            prev_i = nums[i]
            if nums[i] > 0:
                break

            j =  i + 1
            k = len(nums) - 1
            target = -nums[i]
            while j < k:
                print(f'checking {[nums[i], nums[j], nums[k]]}')
                s = nums[j] + nums[k]
                if s == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                elif s < target:
                    j += 1
                else:
                    k -= 1
        
        return res
