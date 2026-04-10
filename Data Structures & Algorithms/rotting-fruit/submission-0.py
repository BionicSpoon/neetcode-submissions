class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        fresh_fruits = 0
        time_passed = 0

        to_rot = [] # to expand rot from, more accurately
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh_fruits += 1
                elif grid[row][col] == 2:
                    to_rot.append((row, col))

        # multi-source BFS - need to spread by one each direction concurrently
        # do this by expanding once in all directions only from tiles in to_rot
        while fresh_fruits > 0 and to_rot:
            new_to_rot = []
            for row, col in to_rot:
                # expand once in each direction
                for dr, dc in directions:
                    nr, nc = row + dr, col + dc
                    if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                        continue
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        new_to_rot.append((nr, nc))
                        fresh_fruits -= 1
                        # don't think we need a visited set/grid or anything else here?
            
            to_rot = new_to_rot
            time_passed += 1
                        
        if fresh_fruits > 0:
            return -1
        else:
            return time_passed
                    

