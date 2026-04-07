class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        ops = []

        for token in tokens:
            if token in '+-*/':
                if token == '+':
                    n2 = int(nums.pop())
                    n1 = int(nums.pop())
                    res = n1 + n2
                elif token == '-':
                    n2 = int(nums.pop())
                    n1 = int(nums.pop())
                    res = n1 - n2
                elif token == '*':
                    n2 = int(nums.pop())
                    n1 = int(nums.pop())
                    res = n1 * n2
                elif token == '/':
                    n2 = int(nums.pop())
                    n1 = int(nums.pop())
                    res = int(n1 / n2)
                nums.append(str(res))


            else:
                nums.append(str(token))
            
            print(nums)

        return int(nums[0])