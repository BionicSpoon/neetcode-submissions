class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l+1, r+1]
            
            if s < target:
                prev_l = numbers[l]
                while l < r and numbers[l] == prev_l:
                    l += 1
            
            else:
                prev_r = numbers[r]
                while r > l and numbers[r] == prev_r:
                    r -= 1
        
        return False
