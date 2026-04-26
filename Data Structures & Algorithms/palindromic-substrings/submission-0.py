class Solution:
    def countSubstrings(self, s: str) -> int:
        # brute force:
        res = len(s)
        for i in range(len(s)):
            for j in range(i+1, len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    res += 1
        return res