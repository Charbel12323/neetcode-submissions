class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # So every 3 rows and 3 columns is a box

        # whatever row were in rows // 3 cols % 3

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]


        for r in range(len(board)):
            for c in range(len(board[0])):

                if board[r][c] == ".":
                    continue
                
                value = board[r][c]
                box_index = (r // 3) * 3 + (c // 3)

                if (value in rows[r]) or (value in cols[c]) or (value in boxes[box_index]):
                    return False
                
                rows[r].add(value)
                cols[c].add(value)
                boxes[box_index].add(value)
        
        return True
                
                

                    