class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # recusively pick any element from the array and make the recursive call
        res = []
        def rec(arr):
            if len(arr) == len(nums):
                res.append(arr.copy())
                return
            for n in nums:
                if n not in arr:
                    arr.append(n)
                    rec(arr)
                    arr.pop()
            
        rec([])
        return res