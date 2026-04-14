class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # bfs from each chest, overwriting values as you go
        # same as rotting oranges p much
        INF = 2 ** 31 - 1
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        treasure = []
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 0:
                    treasure.append((row, col))

        distance = 1
        while treasure:
            print(distance, treasure)
            next_iteration = []
            print(distance, treasure)
            for row, col in treasure:
                val = grid[row][col]
                # expand 1 in all valid directions, then write dist there, then increment distance
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if grid[nr][nc] == INF:
                        grid[nr][nc] = distance
                        next_iteration.append((nr, nc))
                    

            distance += 1
            treasure = next_iteration    

