class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # An island is formed if its connected to any other adjacent island
        # If none of the adjacents islands are unvisited, then that would count as one island

        # No diagonals
        # O(V + E)
        # O(V + E)
        
        # once we visit an unvisited cell (1)
        # if any of the neighbors are also unvisited
        # Then we can add them to the queue
        # To ensure that we dont add the same cell back to the queue
        # We need to mark it as visited (0)
        
        # Once we find a cell that is unvisited and all its neighbors are visited then we can return and increment the count
        # We can use a queue since popping and appending are O(1)

        rows, cols = len(grid), len(grid[0])

        number_islands = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    number_islands += 1
                    queue = deque([(r,c)])
                    grid[r][c] = "0"

                    while queue:
                        r, c = queue.popleft()

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc

                            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                                continue
                            
                            if grid[nr][nc] == "0":
                                continue

                            grid[nr][nc] = "0"
                            
                            queue.append((nr,nc))
                        
        
        return number_islands
                        

                        


