class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Return True if the word thats given exists in the board
        Return False if not

        Recursion would work
        
        plan)
         - iterate through the grid
         - Once we find a character that matches the word is first character
         - We can run dfs for all the adjacent neighbours
         - We need to keep track of the current word that we are building
         - If index == len(word) then we should have a succesfull path
         - We dont need to store the string
         - We dont want infinite recursion so each time we process a cell we must mark it and once we backprop through the recursion we can set it back to what it was before our path so other paths can use it. 

         3^L.mxn
        """

        rows, cols = len(board), len(board[0])
        path = []
        directions = [(1,0),(-1,0),(0,1), (0,-1)]

        def dfs(r,c,i):
            if i == len(word) - 1:
                return True
            
            temp = board[r][c]
            board[r][c] = "#"

            for dr,dc in directions:
                nr, nc = dr + r, dc + c
                if nr < 0 or nr >= rows or nc < 0 or nc >= cols or board[nr][nc] != word[i + 1]:
                    continue
                
                if dfs(nr, nc, i + 1):
                    return True
            
            board[r][c] = temp
            return False


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r,c,0):
                        return True
        
        return False

                    