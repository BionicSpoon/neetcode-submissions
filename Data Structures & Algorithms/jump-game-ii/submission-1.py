class Solution:
    def jump(self, nums: List[int]) -> int:
        # same as jump game I but need to track min
        # instead of bool can_reach array?
        # seems like it, but how to update?
        # if i + nums[i] >= goal:
        #   min_jumps[i] = min_jumps[goal] + 1
        min_jumps = [-1] * len(nums) # min jumps from this point OR FURTHER - monotonic decr
        min_jumps[-1] = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] == 0:
                min_jumps[i] = math.inf
                continue
            max_jump = i + nums[i]
            if i + nums[i] >= len(min_jumps):
                min_jumps[i] = 1
            else:
                min_jumps[i] = min_jumps[max_jump] + 1
                for j in range(i+1, len(min_jumps)):
                    if min_jumps[j] < min_jumps[i]:
                        break
                    min_jumps[j] = min(min_jumps[j], min_jumps[i])
                
        print(min_jumps)
        return min_jumps[0]