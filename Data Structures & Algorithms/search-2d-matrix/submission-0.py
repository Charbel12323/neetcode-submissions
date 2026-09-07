class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        total = rows * cols

        left,right = 0, total - 1

        while left<= right:
            middle = (left + right) // 2

            row = middle // cols
            col = middle % cols
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left += 1
            else:
                right -= 1
        
        return False