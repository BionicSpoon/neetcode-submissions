class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        # make word1 longer
        if len(word2) > len(word1):
            word1, word2 = word2, word1

        dp = [[0 for _ in range(len(word1))] for _ in range(len(word2))]
        
        if not word2:
            return len(word1)

        # setup base row
        j = 1
        for i in range(len(word1)):
            if word1[i] == word2[0]:
                j -= 1
            print(dp[0])
            dp[0][i] = j
            j += 1
        
        for row in range(1, len(word2)):
            for col in range(len(word1)):
                min_edits = math.inf
                min_edits = min(min_edits, (dp[row-1][col-1] + (1 if word1[col] != word2[row] else 0))if col > 0 else math.inf)
                min_edits = min(min_edits, dp[row][col-1] + 1 if col > 0 else math.inf)
                min_edits = min(min_edits, dp[row-1][col] + 1)
                dp[row][col] = min_edits
            
        # for r in dp: print(r)

        return dp[-1][-1]





















#         if len(word1) < len(word2):
#             word1, word2 = word2, word1

#         memo = {}

#         def rec(i1: int, i2: int, operations: int) -> int:
#             if (i1, i2) in memo:
#                 print("memo hit")
#                 return memo[i1, i2]

#             if word1[i1:] == word2[i2:]:
#                 return operations

#             if i2 >= len(word2) and i1 < len(word1):
#                 return operations + len(word1) - i1

#             if i1 >= len(word1) and i2 < len(word2):
#                 return operations + len(word2) - i2

#             if i1 >= len(word1) or i2 >= len(word2):
#                 return operations

#             while i1 < len(word1) and i2 < len(word2) and word1[i1] == word2[i2]:
#                 i1 += 1
#                 i2 += 1

            
#             res = math.inf
#             res = min(res, rec(i1 + 1, i2 + 1, operations + 1)) # as if we overwrote s1 with s2's char
#             res = min(res, rec(i1 + 1, i2, operations + 1)) # as if we deleted s1's char
#             res = min(res, rec(i1, i2 + 1, operations + 1)) # as if we inserted s2's char here

#             memo[(i1, i2)] = res
#
#             return res

#         return rec(0, 0, 0)

