class Solution:
    def recGenerate(self, s, n, opening, closing):
        # print(f'recGenerate({s}, {n}, {opening}, {closing}) called')
        if len(s) == 2 * n and opening == closing:
            print('appending', s, 'to res')
            self.res.append(s)
            return True
        elif len(s) >= 2 * n:
            return False
        elif closing > opening:
            return False

        self.recGenerate(s + '(', n, opening + 1, closing)
        self.recGenerate(s + ')', n, opening, closing + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.res = []
        opening = 1
        closing = 0

        s = '('
        self.recGenerate(s, n, opening, closing)
        return self.res