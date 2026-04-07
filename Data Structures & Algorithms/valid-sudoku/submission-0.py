class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row_base in range(9):
            counts = collections.Counter(board[row_base])
            if '.' in counts: del counts['.']
            if any(counts[k] > 1 for k in counts.keys()):
                return False
        for col in range(9):
            counts = collections.Counter([board[i][col] for i in range(9)])
            if '.' in counts: del counts['.']
            if any(counts[k] > 1 for k in counts.keys()):
                return False
        for x in range(1, 8, 3):
            for y in range(1, 8, 3):
                counts = collections.Counter([board[y][x]]
                                           + [board[y-1][x-1]]
                                           + [board[y-1][x]]
                                           + [board[y-1][x+1]]
                                           + [board[y+1][x-1]]
                                           + [board[y+1][x]]
                                           + [board[y+1][x+1]]
                                           + [board[y][x-1]]
                                           + [board[y][x+1]])
                if '.' in counts: del counts['.']
                if any(counts[k] > 1 for k in counts.keys()):
                    return False
        return True