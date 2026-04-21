class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # real way - start from back
        # and calculate LIS from this idx to the end,
        # and compare it to all LIS starting between here and the end if n < their min
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i+1, len(nums)):
                # [1, 2, 1, 3]
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])

        return max(LIS)


















        # if a 1..n subsequence is increasing:
        # to add element n+1 to the subseq:
        #       case 1: elem n+1 > last (and greatest) element in subseq
        #       case 2: elem n+1 <= last (and greatest) element in subseq
        #       case 1 -> add it to subseq, subseq is 1 longer
        #       case 2 -> replace last elem in subseq with this one
        #               - will strictly yield a subseq >= the old one
        #       is this all? can't be..
        #       store in dp:
        #           dp[n] = (subseq length, subseq elements?) ??
        #       almost - case 2 is wrong here, this will cause invalid seqs if 
        #       the new element < any element in the current subseq
        #       how to fix? how can we tell if this subseq should be overwritten or not?
        #       maybe cannot with bottom-up dp?

        # can we just start at each possible starting index and do this?
        # def dpiter(nums):
        #     print(f"dpiter({nums})")
        #     dp = [0]
        #     dp[0] = (1, [nums[0]])

        #     for num in nums[1:]:
        #         print(dp)
        #         if num > dp[-1][1][-1]:
        #             dp.append((dp[-1][0] + 1, dp[-1][1] + [num]))
                    
        #         elif num <= dp[-1][1][-1]: # and all(num > x for x in dp[-1][1]):
        #             dp.append((dp[-1][0], dp[-1][1][:-1] + [num]))
                    

        #     print(dp)
        #     print("returning", dp[-1][0])
        #     return dp[-1][0]

        # max_len = 0
        # for i in range(len(whole_nums)):
        #     this_iter = whole_nums[i:]
        #     max_len = max(max_len, dpiter(this_iter))

        # return max_len