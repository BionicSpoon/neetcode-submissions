class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # is this not the exact same as subsets I lol?
        # at least my code for it?
        # ANSWER: no lol, [1,2] == [2,1]
        # so, it's another skip duplicates? not quite
        # so, it's a skip the same counts? Yeah, but how?
        # we only want to skip if we skipped 
        # ig it is a skip once we skipped once
        res = []
        nums.sort()

        def rec(i, arr, skipping):
            if i == len(nums):
                res.append(arr.copy())
                return
            
            if skipping == nums[i]:
                rec(i+1, arr, skipping)
                return

            rec(i+1, arr, nums[i])
            arr.append(nums[i])
            rec(i+1, arr, '')
            arr.pop()

        rec(0, [], '')
        return res