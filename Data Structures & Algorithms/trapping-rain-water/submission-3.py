class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        left_maxes = [0 for _ in height]
        right_maxes = [0 for _ in height]
        l_max = 0
        r_max = 0
        for i, h in enumerate(height):
            if i + 1 < len(height):
                l_max = max(l_max, h)
                left_maxes[i+1] = l_max
        for i in range(len(height)-1, 0, -1):
            r_max = max(r_max, height[i])
            right_maxes[i-1] = r_max
        print(left_maxes, right_maxes)
        for i, h in enumerate(height):
            if h < min(left_maxes[i], right_maxes[i]):
                total += min(left_maxes[i], right_maxes[i]) - h
            # print(f'index {i}: {min(left_maxes[i], right_maxes[i]) - h}')
        

        return total