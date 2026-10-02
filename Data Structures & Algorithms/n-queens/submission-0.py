class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        result = []

        cols = set()
        pos_diag = set()   # row + col
        neg_diag = set()   # row - col

        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            # Successfully placed queens in all n rows
            if row == n:
                result.append(["".join(r) for r in board])
                return

            for col in range(n):

                # Check if queen would attack another queen
                if (
                    col in cols
                    or (row + col) in pos_diag
                    or (row - col) in neg_diag
                ):
                    continue

                # Choose
                cols.add(col)
                pos_diag.add(row + col)
                neg_diag.add(row - col)
                board[row][col] = "Q"

                # Explore
                backtrack(row + 1)

                # Undo
                cols.remove(col)
                pos_diag.remove(row + col)
                neg_diag.remove(row - col)
                board[row][col] = "."

        backtrack(0)
        return result