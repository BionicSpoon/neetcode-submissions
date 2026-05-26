class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # just start from each starting letter (first char in word)
        # and make a recursive call to each adjacent cell if it is the next char
        ROWS, COLS = len(board), len(board[0])
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def rec(i, j, word_i, seen) -> bool:
            # return whether word can be formed from here
            # printi, j, word_i, list(seen))
            if word_i >= len(word) - 1:
                return True
            
            for dr, dc in dirs:
                # printdr, dc)
                nr, nc = i + dr, j + dc
                # print"new:", nr, nc)
                if (nr, nc) not in seen and nr < ROWS and nr >= 0 and nc < COLS and nc >= 0:
                    # print"checking", nr, nc)
                    if board[nr][nc] == word[word_i + 1]:
                        seen.append((i, j))
                        # printseen)
                        if rec(nr, nc, word_i + 1, seen):
                            return True
                        seen.pop()

                        
            return False

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and rec(r, c, 0, []):
                    return True

        return False