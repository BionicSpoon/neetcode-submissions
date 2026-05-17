class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # CAN you reach the last idx starting from idx 0?
        # check all paths?
        # start from the end and go backwards? seems hard tho
        # explore all path, keep a secondary arr (or overwrite nums) with bools
        # dp: go from the back, and store whether each tile can reach the end
        # backfill by checking if this tile can reach a valid one
        can_reach = [False] * (len(nums) - 1) + [True]
        for i in range(len(nums) - 2, -1, -1):
            for j in range(nums[i], 0, -1):
                if i+j < len(can_reach) and can_reach[i+j]:
                    can_reach[i] = True
                    break
            
        return can_reach[0]



            
