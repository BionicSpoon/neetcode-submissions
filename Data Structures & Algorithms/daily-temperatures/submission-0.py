class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        cur_temp = float("infinity")
        for i, temp in enumerate(temperatures):
            if temp <= cur_temp:
                cur_temp = temp
                
            else:
                while stack and stack[-1][1] < temp:
                    res[stack[-1][0]] = i - stack[-1][0]
                    stack.pop()

            stack.append((i, temp))
                

        return res