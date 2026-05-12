class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # same as the last one, but you either go next and add this
        # or go next and don't add this
        candidates.sort()
        print(candidates)

        res = []
        # add another var to track the current char being skipped (after it has been skipped once)
        def rec(i, subtotal: List[int], path, skipping):
            if subtotal == target:
                res.append(path.copy())
                return
            if i > len(candidates) - 1 or subtotal > target:
                return

            if candidates[i] == skipping:
                rec(i+1, subtotal, path, candidates[i])
                return

            path.append(candidates[i])
            rec(i+1, subtotal + candidates[i], path, '')
            path.pop()
            rec(i+1, subtotal, path, candidates[i])
            

        rec(0, 0, [], '')
        return res