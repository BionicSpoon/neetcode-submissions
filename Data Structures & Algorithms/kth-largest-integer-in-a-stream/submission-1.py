class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify_max(self.heap)
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush_max(self.heap, val)
        # print(self.heap)
        return heapq.nlargest(self.k, self.heap)[-1]
