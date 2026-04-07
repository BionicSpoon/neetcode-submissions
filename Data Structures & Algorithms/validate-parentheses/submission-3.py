class Solution:
    def isValid(self, s: str) -> bool:
        parens = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{',
            }
        for p in s:
            if p in pairs.values():
                parens.append(p)
            elif len(parens) > 0 and parens[-1] == pairs[p]:
                parens.pop()
            else:
                return False
        return not parens