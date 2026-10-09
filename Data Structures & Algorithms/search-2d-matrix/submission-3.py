class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # M x N 
        # We can use binary search to make it log(m*n)
        # 12 // m = n  
        # m x n flatten out matrix. left  = 0 and right = mxn. 

        #middle then we can covert the middle to row and column such that
        # row = middle // n and col == middle /m check condition and then update as necessary

        # log(m*n)
        # O(1)

        rows = len(matrix)
        cols = len(matrix[0])

        total = rows * cols

        left, right = 0, total - 1

        while left <= right:
            middle = (left + right) // 2

            row = middle // cols # 
            col = middle % cols

            if matrix[row][col] > target:
                right = middle - 1
            elif matrix[row][col] < target:
                left = middle + 1
            else:
                return True
        
        return False