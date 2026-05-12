from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache
        def rec(i, j, prev) -> bool:
            if i == len(s) and j == len(p):
                return True
            if i == len(s) and j == len(p) - 2 and p[j+1] == '*':
                return True
            if i >= len(s) or j >= len(p):
                return False
            
            if p[j] == '.':
                return rec(i + 1, j + 1, '.')
            
            if p[j] == '*':
                if prev == '.':
                    # take it or skip it
                    return rec(i + 1, j, '.') or rec(i + 1, j + 1, '')
                else:
                    # prev == char, use it again or skip it
                    print("in else", i, j, prev)
                    take = False
                    if s[i] == prev:
                        take = rec(i + 1, j, prev) or rec(i, j + 1, '')
                    else:
                        return rec(i, j + 1, '')
                    return take or rec(i + 1, j + 1, '')

            elif s[i] == p[j]:
                return rec(i + 1, j + 1, s[i]) or rec(i, j + 2, '*')
            
            else:
                if j + 1 < len(p) and p[j + 1] == '*':
                    return rec(i, j + 1, '')
                return False

        return rec(0, 0, '')

