class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        max_area = 0

        def dfs(r,c):
            area = 0
            grid[r][c] = 0

            for dr,dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                if grid[nr][nc] == 0:
                    continue
                
                area += dfs(nr,nc)
            
            return 1 + area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area