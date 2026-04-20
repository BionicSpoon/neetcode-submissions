class Solution:
    def rob(self, nums: List[int]) -> int:
        # same as house robber I - BUT you can't rob both the first and last house
        # dp array to find max robbable at each house?
        # most of the problem is the same right? - or is it?
        # Can you do something like adding the first house to the end of the array?
        # 2 cases: rob inside to get max, and add max(first, last)?
        # rob first->second to last and second-> last seperately?
        # this seems promising - return the max of these two paths
        # maybe could be more efficient, but let's try it
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        max_rob = [0] * (len(nums) - 1)
        max_rob[0], max_rob[1] = nums[0], max(nums[0], nums[1])

        last = nums[-1]
        nums = nums[:-1]

        for i in range(2, len(nums)):
            # at each house, either rob it and take i-2, or don't and take i-1,
            # whichever is greater
            max_rob[i] = max(max_rob[i-1], max_rob[i-2] + nums[i])

        best_rob = max_rob[-1]


        nums.append(last)
        nums = nums[1:]

        max_rob[0], max_rob[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            max_rob[i] = max(max_rob[i-1], max_rob[i-2] + nums[i])


        return max(best_rob, max_rob[-1])