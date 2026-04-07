class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = ''.join(sorted(s1))

        for i in range(len(s2) - len(s1) + 1):
            sub = ''.join(sorted(s2[i:i+len(s1)]))
            print(sub, s1)
            if sub == s1:
                return True
        return False