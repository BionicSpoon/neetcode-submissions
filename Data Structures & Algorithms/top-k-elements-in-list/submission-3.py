class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        print(counts)
        res = [0] * k
        frequencies = [0] * k
        i = 0
        for num in counts:
            if i < len(res):
                res[i] = num
                frequencies[i] = counts[num]
                i += 1
            else:
                c = frequencies.index(min(frequencies))
                if counts[num] > frequencies[c]:
                    frequencies[c] = counts[num]
                    res[c] = num    
            
        return res