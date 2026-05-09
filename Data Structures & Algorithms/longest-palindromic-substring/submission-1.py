class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def expandFrom(center):
            # assuming odd palindrome
            left = center
            right = center
            length = 0
            while True:
                if left < 0 or right >= len(s) or s[left] != s[right]:
                    length = right - left - 1
                    break
                left -= 1
                right += 1
            substr = s[left+1:right]
            # even palindrome
            left = center
            right = center + 1
            while True:
                if left < 0 or right >= len(s) or s[left] != s[right]:
                    if right - left - 1 > length:
                        length = right - left - 1
                        substr = s[left+1:right]
                    break
                left -= 1
                right += 1

            return length, substr
            
        longest = 0
        longest_substr = ''
        for i in range(len(s)):
            l, res = expandFrom(i)
            if l > longest:
                longest = l
                longest_substr = res

        return longest_substr