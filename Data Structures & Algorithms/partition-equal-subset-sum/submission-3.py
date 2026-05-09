class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # brute force: generate all possible pairs of subsets
        # by putting each number in either subset1 or subset2

        # slightly less brute force:
        # nvm, arr could be [1, 1, 1, ..., 100]
        # how to do dp here? Not sure really
        # after hint: Use recursion to try to form a subset with a sum of half the total sum
        # Then, we can return whether or not this is possible?
        half_sum = sum(nums) / 2
        if sum(nums) % 2:
            return False
        half_len = len(nums) / 2
        memo = {}
        def rec(i, subtotal, ns) -> bool:
            if i >= len(nums) or ns > half_len:
                return subtotal == half_sum

            if (i, subtotal, ns) in memo:
                return memo[(i, subtotal, ns)]
            
            res = rec(i + 1, subtotal + nums[i], ns + 1) or rec(i + 1, subtotal, ns)
            memo[(i, subtotal, ns)] = res
            return res

        return rec(0, 0, 0)