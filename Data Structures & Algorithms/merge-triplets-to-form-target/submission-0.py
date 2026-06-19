class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # observations:
        # merging two triplets can ONLY increase values
        # 

        # we prob have to sort
        # but where to start?
        # which one to take each time?

        # keep a current sum
        # if merging with each triplet would take it over any max, don't
        # else, do?
        # seems about right
        cur = [0, 0, 0]
        for x, y, z in triplets:
            if x > target[0] or y > target[1] or z > target[2]:
                continue
            cur = [max(cur[0], x), max(cur[1], y), max(cur[2], z)]
        
        return cur == target