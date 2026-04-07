class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if h == len(piles):
            return max(piles)

        # piles.sort()
        l = 1
        r = max(piles)
        min_k = r
        while l <= r:
            k = (l + r) // 2
            good = True
            hours_used = 0
            for i in range(len(piles)):
                hours_used += math.ceil(piles[i] / k)
            print(k, hours_used)
            if hours_used == h:
                min_k = min(k, min_k)
                r = k - 1
            elif hours_used < h:
                min_k = min(k, min_k)
                r = k - 1
            else:
                l = k + 1



        return min_k
                




        i = len(piles) - 1 - h
        h -= len(piles)
        prev_i = 0
        loops = 0
        while h:
            prev_i = i
            i = (i - 1) % len(piles)
            if i > prev_i:
                loops += 1
            h -= 1
        
        return piles[i] // loops + 1


        # each "eat" is defined as:
        piles[i] = max(piles[i] - k, 0)

        # time to eat a pile is:
        time_to_eat[i] = math.ceil(piles[i] / k)
        