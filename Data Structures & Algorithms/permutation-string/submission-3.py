class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target_freq = Counter(s1)
        freq = Counter(s2[0:len(s1)])
        if target_freq == freq:
            return True
        r = len(s1)
        l = 0
        while r < len(s2):
            freq[s2[l]] -= 1
            if freq[s2[l]] == 0:
                del freq[s2[l]]
            freq[s2[r]] = 1 + freq.get(s2[r], 0)
            if target_freq == freq:
                return True
            l += 1
            r += 1

        print(target_freq, freq)
        if target_freq == freq:
            return True
            
        return False
        
        s1 = ''.join(sorted(s1))

        for i in range(len(s2) - len(s1) + 1):
            sub = ''.join(sorted(s2[i:i+len(s1)]))
            print(sub, s1)
            if sub == s1:
                return True
        return False