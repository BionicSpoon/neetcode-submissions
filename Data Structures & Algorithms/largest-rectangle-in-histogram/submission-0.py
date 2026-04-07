class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # ONLY POPPING THE MOST RECENT ELEMENTS
        # -> WE SHOULD USE A STACK
        max_area = 0    
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                l, prev_h = stack.pop()
                max_area = max(max_area, (i - l) * (prev_h))
                start = l


            stack.append((start, h))

        for i, h in stack:
            max_area = max(max_area, (len(heights) - i) * h)

        return max_area







        left_stack = [heights[0]]
        left_expansion = [0 for _ in range(len(heights))]
        for i in range(1, len(heights)):
            # print(left_expansion)
            if heights[i] == heights[i-1]:
                left_expansion[i] = left_expansion[i-1] + 1
            elif heights[i] > heights[i-1]:
                left_expansion[i] = 0
            else:
                # print(f'entered else; {i=}')
                left_expansion[i] = left_expansion[i-1]
                # print(left_stack, heights[i])
                while left_stack and left_stack[-1] >= heights[i]:
                    # print('adding one at i =', i)
                    left_stack.pop()
                    left_expansion[i] += 1
            left_stack.append(heights[i])
        
        right_stack = [heights[-1]]
        right_expansion = [0 for _ in range(len(heights))]
        for i in range(len(heights) - 2, -1, -1):
            # print(right_expansion)
            if heights[i] == heights[i+1]:
                right_expansion[i] = right_expansion[i+1] + 1
            elif heights[i] > heights[i+1]:
                right_expansion[i] = 0
            else:
                # print(f'entered else; {i=}')
                right_expansion[i] = right_expansion[i+1]
                print(right_stack, heights[i])
                diff = 0
                while right_stack and right_stack[-1] > heights[i]:
                    # print('adding one at i =', i)
                    if i == len(heights) - 2:
                        right_expansion[i] += 1
                        break
                    right_stack.pop()
                    right_expansion[i] += 1
                    diff += 1
                if right_stack and right_stack[-1] == heights[i]:
                    right_expansion[i] += right_expansion[i+diff]
            right_stack.append(heights[i])

        

        print(f'{left_expansion=}')
        print(f'{right_expansion=}')



        return max_area
