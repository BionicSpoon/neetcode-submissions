class Solution:
    def reverseBits(self, n: int) -> int:
        # print(n)
        # n = bin(n)
        # n = n[2:]
        # n = '0' * (32 - len(n)) + n
        # print(n, len(n))
        res = 0
        for i in range(32):
            if n & (1 << i):
                res |= (1 << (31 - i))
        return res