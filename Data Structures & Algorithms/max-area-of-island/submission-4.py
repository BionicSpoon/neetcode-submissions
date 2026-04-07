class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        islands = 0
        visited = set()
        max_area = 0
        iteration = 0
        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if grid[row_idx][col_idx] == 0:
                    continue
                coords = (row_idx, col_idx)
                if coords not in visited:
                    #print(f"----------ITERATION {iteration}---------; {max_area=}")
                    islands += 1

                    # mark this island as visited - BFS
                    queue = [coords]
                    cur_area = 0
                    while queue:
                        #print(queue, max_area)
                        # for l in grid:
                            #print(l)
                        cur = queue.pop(0)
                        
                        grid[cur[0]][cur[1]] = 0
                        cur_area += 1
                        #print(f'adding to {cur_area=}')
                        visited.add(cur)
                        # ONLY add non-visited coords to the queue
                        neighbors = [(cur[0] - 1, cur[1]),
                                     (cur[0] + 1, cur[1]),
                                     (cur[0], cur[1] - 1),
                                     (cur[0], cur[1] + 1)]

                        for neighbor in neighbors:
                            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 1 and neighbor not in visited:
                                queue.append(neighbor)
                                grid[neighbor[0]][neighbor[1]] = 0
                    
                    max_area = max(max_area, cur_area)
                    iteration += 1

        return max_area