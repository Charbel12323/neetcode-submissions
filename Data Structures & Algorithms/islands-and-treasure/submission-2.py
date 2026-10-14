class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # -1 if a cell contains this we cant traverse
        # Were going to iterate through the grid and store all the rows and columns of the treasure cells
        # We will store them in queue because we wnat them to be ordered by when they were found and we also want O(1) when retrieiving these columns
        # Then for each column we can go to each adjavent neighbor
        # If the adjacent neighbor is out of boundaries or is a treasure or is a -1 cell. We dont add it to the queue
        # If all of these are false, then we can updat ethe value of the new cell by the increment of the previous value
        # We are guaranteed to have the smallest distance treasure since we were able to make it to the empty cell first. 

        rows, cols = len(grid), len(grid[0])
        queue = deque()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
        
        while queue:
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                    continue
                
                if grid[nr][nc] != 2147483647:
                    continue
                    
                grid[nr][nc] = grid[r][c] + 1

                queue.append((nr, nc))
        

                


