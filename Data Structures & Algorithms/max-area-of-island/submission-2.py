class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # ONce we visit an unvisited cell
        # We add that cell to the queue
        # And then we look at all adjacent neighbours
        # We first check if that neighbor is out of boundaries or already viisted
        # If neither ar eture
        # Then we add that neighbour to the que
        # Everytrim we process a node, we add 1 to the area
        # and then comapre it with the maximum area once are queue is empty
        
        rows, cols = len(grid), len(grid[0])
        max_area = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    queue = deque([(r,c)])
                    grid[r][c] = 0
                    area = 0
                    while queue:
                        r,c = queue.popleft()

                        area += 1

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc

                            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                                continue
                            
                            if grid[nr][nc] == 0:
                                continue
                            
                            grid[nr][nc] = 0

                            queue.append((nr,nc))

                    max_area = max(max_area, area)
        
        return max_area


