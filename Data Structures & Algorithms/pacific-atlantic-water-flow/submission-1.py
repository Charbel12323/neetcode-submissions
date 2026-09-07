class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        # Our main rule is that if current_height < prev height then we are good
        rows, cols = len(heights), len(heights[0])

        def dfs(r,c,visited, prev_height):
            if r < 0 or r >= rows or c < 0 or c >= cols or heights[r][c] < prev_height or (r,c) in visited:
                return
            
            visited.add((r,c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                dfs(nr, nc, visited, heights[r][c])
            
        # Lets start with the top and bottom row
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])
            dfs(rows -1, c, atlantic, heights[rows-1][c])
        
        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, cols -1, atlantic, heights[r][cols-1])
        
        results = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific and (r,c) in atlantic:
                    results.append((r,c))
        
        return results