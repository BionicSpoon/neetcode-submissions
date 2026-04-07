class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        longest = 0
        l = 0
        for i, char in enumerate(s):
            if char not in chars:
                chars.add(char)
                longest = max(longest, len(chars))
            else:
                print(s[l], char, chars)
                while l < i and s[l] != char:
                    print(longest)
                    print(f'removing {s[l]} from {chars}')
                    chars.remove(s[l])
                    l += 1
                l += 1
        return longest
