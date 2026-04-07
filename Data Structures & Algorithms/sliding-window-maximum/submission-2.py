class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        nums = [-num for num in nums]
        h = [(nums[i], i) for i in range(k)]
        heapq.heapify(h)
        print(h)
        res.append(-h[0][0])
        
        l = 1
        for r in range(k, len(nums)):

            heapq.heappush(h, (nums[r], r))

            while h[0] and h[0][1] < l:
                heapq.heappop(h)
            res.append(-h[0][0])



            l += 1

        return res




        # if k == 1:
        #     return nums
        # maxn = -100000
        # second_max = -100000
        # counts = {}
        # res = []
        # l = 0
        # for i in range(k):
        #     counts[nums[i]] = 1 + counts.get(nums[i], 0)
        #     if nums[i] > maxn:
        #         if maxn > second_max:
        #             second_max = maxn
        #         maxn = nums[i]
        
        # res.append(maxn)

        # for r in range(k, len(nums)):
        #     counts[nums[r]] = 1 + counts.get(nums[r], 0)
        #     if nums[r] > maxn:
        #         if maxn > second_max:
        #             second_max = maxn
        #         maxn = nums[r]

        #     counts[nums[l]] -= 1
        #     if counts[nums[l]] == 0 and nums[l] == maxn:
        #         maxn = second_max
        #     l += 1


        #     res.append(maxn)


            
            
        
        # print(f'{maxn=}, {second_max=}')
        # return res


        