class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            res += str(len(string)) + '#' + string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s) - 1:
            length = ''
            while s[i] != '#':
                length += s[i]
                i += 1
            length = int(length)
            i += 1
            cur = ''
            for _ in range(length):
                cur += s[i]
                i += 1
            res.append(cur)

    
        return res
