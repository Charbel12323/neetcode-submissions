class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        max_area = 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
                return 0
            
            area = 1

            grid[r][c] = 0

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                area += dfs(nr, nc)

            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = dfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area