class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        
        l_maxes = [0]
        l_max = 0
        for i in range(1, len(height)):
            l_max = max(l_max, height[i-1])
            l_maxes.append(l_max)
        print(f'{l_maxes=}')
        r_maxes = [0] * len(height)
        r_max = 0
        for i in range(len(height) - 2, -1, -1):
            r_max = max(r_max, height[i+1])
            r_maxes[i] = r_max
        print(f'{r_maxes=}')

        total = 0
        max_so_far = 0
        for i, h in enumerate(height):
            total += max(min(l_maxes[i], r_maxes[i]) - h, 0)
            

        return total