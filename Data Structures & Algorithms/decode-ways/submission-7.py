class Solution:
    def numDecodings(self, code: str) -> int:
        valid = set(str(n) for n in range(1, 27))
        ways = 0
        memo = {}
        
        def rec(s: str) -> int:
            nonlocal ways
            if not s:
                ways += 1
                return 0
            if s[0] == '0':
                return 0
            if len(s) == 1:
                ways += 1
                return 1
            
            if s[1:] in memo:
                ways += memo[s[1:]]
            else:
                prev = ways
                rec(s[1:])
                memo[s[1:]] = ways - prev
                
            if s[:2] in valid:
                if s[2:] in memo:
                    ways += memo[s[2:]]
                else:
                    prev = ways
                    rec(s[2:])
                    memo[s[2:]] = ways - prev

            return 0

        rec(code)
        return ways



