class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        def recSubsets(i: int, nums: List[int], path: List[int]) -> List[int]:
            # at each iteration, both add the number at i to path or skip it, call recursively for both
            # print(f'recSubsets({i}, {nums}, {path}) just called')
            if i >= len(nums):
                res.append(path)
                return

            recSubsets(i+1, nums, path[:])
            recSubsets(i+1, nums, path[:] + [nums[i]])
            
        recSubsets(0, nums, [])
            

        return res