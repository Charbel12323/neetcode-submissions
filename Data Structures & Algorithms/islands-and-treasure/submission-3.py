class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        while queue:
            row, col = queue.popleft()

            for dr, dc in directions:
                nr,nc = row + dr, col + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                if grid[nr][nc] != 2147483647:
                    continue
                
                grid[nr][nc] = grid[row][col] + 1
                queue.append((nr,nc))
        
    
        
        
