class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        max_area = 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
                return 0
            
            area = 1

            grid[row][col] = 0

            for dr, dc in directions:
                nr, nc = dr + row, dc + col
                area += dfs(nr, nc)
            
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    max_area = max(max_area, dfs(r,c))
        
        return max_area
