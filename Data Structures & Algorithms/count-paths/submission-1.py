class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # IM given an mxn grid where I can move either down or right
        # You would like me to find the number of possible unieque path take until we reach the bottom right of the grid

        # Since I can move either right or down, this means the frist and first column willl only have 1 uniquee way.
        # My brute solution would be to start from the bottmo right. And move either left or up. As long as the row or column dont pass the edge cases.
        # We would do keep recursing until we make it to eh top left of the grid

        # Clearly there are going to be overlapping subproblems since we might be caluclating the number of ways for one index multiple times.

        # dp[i][j] = dp[i-1][j] + dp[i][j - 1]

        # We could use memoization to store the number of ways per index so we dont have to that again giving us a time complexity of (mxn) but space(mxn)

        # Clearly as we can see from our equations we dont really need the whole table. All we need is the previous row and the previous column to figure out.

        dp = [[1] * (n) for _ in range(m)]

        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]