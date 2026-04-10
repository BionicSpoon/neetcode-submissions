class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 1. The only time an O cannot be turned into an X is if it cannot reach
        # any edge of the board through a path of O's
        # 2. Brute force: Check each O for whether or not it can reach an edge w/ backtracking
        # If not, change it to an X; rinse and repeat.
        # 3. Much less brute force: If it CANNOT reach the edge, do ANOTHER dfs from the
        # tile, changing all Os to Xs

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                # 1. Check if an edge can be reached from here
                if board[row][col] == "X":
                    continue
                group = set()
                edge_reached: bool = False
                # let's do BFS
                queue = [(row, col)]
                while queue:
                    cur_row, cur_col = queue.pop(0)
                    group.add((cur_row, cur_col))

                    for dr, dc in directions:
                        nr, nc = cur_row + dr, cur_col + dc
                        if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                            edge_reached = True # for this group
                            continue
                        if (nr, nc) not in group and board[nr][nc] == "O":
                            queue.append((nr, nc))

                if not edge_reached:
                    for r, c in group:
                        board[r][c] = 'X'
                        
