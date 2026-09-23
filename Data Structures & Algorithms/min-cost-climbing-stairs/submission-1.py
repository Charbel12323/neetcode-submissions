class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost) #[1,2,3] n = 3
        dp = [0] * (n + 1) # [0,0,0,0]

        # The cost for floor 1 and floor 2 are both 0 since thats where we are starting from
        # So we must start on floor 3 -> 2

        for i in range(2, n + 1): # [1,2,3] n = 3 n = 4 0,1,2,3(top floor)
            dp[i] = min(dp[i-1] + cost[i-1], dp[i-2] + cost[i - 2])
        
        return dp[n]