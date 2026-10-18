class Solution:
    def climbStairs(self, n: int) -> int:

        # can n = 0
        # n +1 represents the top of the staircase
        # 45 

        # That each step we could either take 1 step or 2 steps
        # n + 1 is the top of the stair case

        # n = 3

        # come from step 1 or step 2
        # To get  tp step2, ic ould come from step 1 or step 0

        # numberOfWays(n) = numberOfWays(n - 1) + numberOfWays(n - 2)

        # Time and space O(2^n)

        # Psuedcode
        # memo = {} # stepNum : NumOfWays
        # 
        # def dfs(i):
        #   if i in memo:
        #       return memo[i]

        #   if i < 0:
        #       return 0
        #   
        #   numberOfWays = dfs(i - 1) + dfs(i - 2)
        #   memo[i] = 1 + numberOfWays
        #   return memo[i]

        # prev1 = 1
        # prev2 = 2
        
        # for i in range(n + 1):
        #     temp = prev1
        #     prev1 = prev1 + prev2
        #     prev2 = temp
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        prev1 = 2
        prev2 = 1

        for i in range(3, n + 1):
            temp = prev1
            prev1 = prev2 + prev1
            prev2 = temp
        
        return prev1


