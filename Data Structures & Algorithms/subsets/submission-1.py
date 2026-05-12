class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def rec(i, arr):
            # either skip or take
            if i >= len(nums):
                res.append(arr.copy())
                return

            rec(i+1, arr)
            arr.append(nums[i])
            rec(i+1, arr)
            arr.pop()

        rec(0, [])
        return res