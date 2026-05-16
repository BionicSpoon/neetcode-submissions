class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # make a heap with [(distance, [xi, yi]] as entries? This will sort by distance
        # in O(n)? nah nlogn for heapsort'
        # but transforming an unsorted array into heap only takes O(n)
        # So, the sort becomes O(nlogn) because the logn comes from extracting each element in logn time
        # so, it will be O(n * k) for sort -> get k points

        q = []
        for x, y in points:
            q.append(((x**2 + y ** 2), [x, y]))

        res = []
        heapq.heapify(q)
        for _ in range(k):
            point = heapq.heappop(q)[1]
            res.append(point)
        return res
