class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()

        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if grid[row_idx][col_idx] == '0':
                    continue
                coords = (row_idx, col_idx)
                if coords not in visited:
                    islands += 1

                    # mark this island as visited - BFS
                    queue = [coords]
                    while queue:
                        cur = queue.pop(0)
                        visited.add(cur)
                        # ONLY add non-visited coords to the queue
                        neighbors = [(cur[0] - 1, cur[1]),
                                     (cur[0] + 1, cur[1]),
                                     (cur[0], cur[1] - 1),
                                     (cur[0], cur[1] + 1)]

                        for neighbor in neighbors:
                            if neighbor not in visited and 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == '1':
                                queue.append(neighbor)

        return islands