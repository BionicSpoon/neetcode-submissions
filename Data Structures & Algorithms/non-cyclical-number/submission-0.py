class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            total = 0
            for digit in str(n):
                digit = int(digit)
                total += digit ** 2
            n = total
            if n == 1:
                break
        return n == 1