class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # same concept as last time right?
        # maintain a minheap
        # and limit it to k elements
        # boom, O(n * logk) idk where the logk comes from
        # logk because the extraction/insert time is log(height), and height is max k
        q = nums[:k]
        heapq.heapify(q)
        for i in range(k, len(nums)):
            heapq.heappush(q, nums[i])
            if len(q) > k:
                heapq.heappop(q)

        return q[0]
