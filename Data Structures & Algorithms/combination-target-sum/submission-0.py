class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # either take or skip each number
        # make rec(i, subtotal) -> List[List[int]]
        #       -> take: rec(i, subtotal + nums[i])
        #       -> skip: rec(i+1, subtotal)
        # append all lists of combination sums to result, return it

        def rec(i: int, subtotal: int, path: tuple[int]) -> List[List[int]]:
            # print(path)
            res = []
            if subtotal == target:
                res.append(list(path))
                return res
            
            if i > len(nums) - 1 or subtotal > target:
                return []
            
            take = rec(i, subtotal + nums[i], path + (nums[i],))
            skip = rec(i+1, subtotal, path)
            if take:
                for t in take:
                    res.append(t)
            if skip:
                for s in skip:
                    res.append(s)
            
            # print(res)
            return res

        return rec(0, 0, ())