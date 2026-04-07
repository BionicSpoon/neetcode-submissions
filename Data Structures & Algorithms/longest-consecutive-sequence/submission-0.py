class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in nums:
                cur = 0
                while num in nums:
                    cur += 1
                    num += 1
                longest = max(longest, cur)
        return longest