class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        Return the maximum area - Largest island
        1) We dont count diagonals
        2) the maximum length of the grid is going to be 100
        3) Assume if the grid is empty -> return area of 0

        Solution1) - DFS
        """

        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1),(0,-1)]
        max_area = 0

        def bfs(r,c):
            queue = deque([(r,c)])
            grid[r][c] = 0
            area = 1

            while queue:
                r,c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    
                    if grid[nr][nc] == 0:
                        continue
                    
                    grid[nr][nc] = 0

                    area += 1
                    queue.append((nr,nc))
            
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    area = bfs(r,c)
                    max_area = max(max_area, area)
        
        return max_area
