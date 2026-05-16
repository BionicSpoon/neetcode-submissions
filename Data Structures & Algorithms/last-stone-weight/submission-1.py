class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)

        while len(stones) > 1:
            stone_1 = heapq.heappop_max(stones)
            stone_2 = heapq.heappop_max(stones)
            new_stone = stone_1 - stone_2
            if new_stone:
                heapq.heappush_max(stones, new_stone)
        
        return stones[0] if stones else 0