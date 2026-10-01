class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        result = []
        path = []

        def backtrack(row, col, index):
            if index == len(word):
                return True
            
            if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
                return False
            
            if board[row][col] != word[index]:
                return False
            
            temp = board[row][col]
            board[row][col] = "tmp"
            
            found = (backtrack(row + 1, col, index + 1) or backtrack(row-1, col, index + 1)
            or backtrack(row, col + 1, index + 1) or backtrack(row, col -1, index + 1))

            board[row][col] = temp

            return found
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    found = backtrack(r,c,0)
                    if found == True:
                        return True

        return False        


