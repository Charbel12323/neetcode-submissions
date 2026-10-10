class Solution:
    def climbStairs(self, n: int) -> int:
        # Brute force solution
        # WE can use recursion where each recursive call calculates (n-1) and (n - 2)
        # 3 -> NW(2) - NW (1)
        # NW(2) -> NW(1) # Overlapping subroplmen right ehere

        # Issue with this is we are recaculating the subproblem and since we have 2 choices its the time complexity is going to be 2^n
        
        # We can optimize this using memoization. So rather than calculating the same sub problems, we can store them in a cache (dictionary) to check if it exists if it does we just return that answer
        if n == 1:
            return 1
        
        if n == 2:
            return 2

        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):

            dp[i] = dp[i-1] + dp[i - 2]
        
        return dp[n]


            