class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # brute force: take a char from either s1 or s2 at each option
        # represent this with two indices (two pointers, basically)
        # add memoization and should be ggez, right?

        # return True if the combination of indices is a valid interleaving
        # (if any of the VALID TO MAKE recursive calls is True)
        memo = {}
        def rec(i1: int, i2: int, i3: int) -> bool:
            if i3 == len(s3) and i1 == len(s1) and i2 == len(s2):
                return True
            elif i3 >= len(s3):
                return False

            if (i1, i2, i3) in memo:
                return memo[(i1, i2, i3)]

            res = False
            if i1 < len(s1) and s1[i1] == s3[i3]:
                res = rec(i1 + 1, i2, i3 + 1)

            if i2 < len(s2) and s2[i2] == s3[i3]:
                res = res or rec(i1, i2 + 1, i3 + 1)

            memo[(i1, i2, i3)] = res
            return res

        return rec(0, 0, 0)