class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # have to bfs/dfs from each cell, and determine whether or not water can reach each ocean
        # we must be careful about only moving to cells with height <= current cell's height
        ROWS, COLS = len(heights), len(heights[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        res = []

        # 0 if cannot reach; 1 if can reach
        pacific = [[0 for _ in range(COLS)] for _ in range(ROWS)]
        atlantic = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        # need to determine which oceans or both are reachable
        # let's do a dfs looking for each ocean - NO
        # just expand from each edge tile and mark reachable tiles from each ocean
        # in their respective ocean grids
        # Called from each border tile
        def dfs(row, col, ocean):
            # already visited if pacific or atlantic grid space is 1
            print(f"dfs({row}, {col}, {ocean})")
            if ocean == "Pacific":
                pacific[row][col] = 1
            else:
                atlantic[row][col] = 1

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if nr < 0 or nc < 0:
                    continue
                elif nr >= ROWS or nc >= COLS:
                    continue
                
                # print(f"valid coords: ({nr}, {nc})")
                # print(heights[nr][nc], heights[row][col])
                if heights[nr][nc] >= heights[row][col]:
                    # print("in if")
                    if ocean == "Pacific" and pacific[nr][nc] != 1:
                        dfs(nr, nc, ocean)
                    elif ocean == "Atlantic" and atlantic[nr][nc] != 1:
                        dfs(nr, nc, ocean)

            
            
        # Test on (0, 3)     - good debugging hack
        # dfs(0, 3, "Pacific")
            

        # let's do DFS
        for row in range(ROWS):
            for col in range(COLS):
                if row == 0 or col == 0:
                    dfs(row, col, "Pacific")
                if row == ROWS - 1 or col == COLS - 1:
                    dfs(row, col, "Atlantic")

        print("Can reach Pacific:")
        print(pacific)
        print("Can reach Atlantic:")
        print(atlantic)

        for row in range(ROWS):
            for col in range(COLS):
                if pacific[row][col] == 1 and atlantic[row][col] == 1:
                    res.append([row, col])

        return res