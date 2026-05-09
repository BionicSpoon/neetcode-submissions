class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            ones = 0
            while i > 0:
                ones += 1 if i & 1 else 0
                i >>= 1
            res.append(ones)
        return res