class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # What is a minute? A minute is represented by all the current rotten tomatoes ahve infected the other ones
        # When do we stop? We stop when there are no longer any fresh bananas
        # If there is one rotten banana, then there shal be no fresh remaining
        
        fresh = 0
        rows, cols = len(grid), len(grid[0])
        queue = deque() # Pop the left side first

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append((r,c))

        minutes = 0

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        while queue and fresh > 0:
            for _ in range(len(queue)): # This is considered as a minumte
                row, col = queue.popleft()


                
                for dr,dc in directions:
                    nr, nc = row + dr, col + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        continue
                    
                    if grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        queue.append((nr, nc))

            minutes += 1
        
        return minutes if fresh == 0 else -1
                    


                