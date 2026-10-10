class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # I have 2 options either go up one or 2 stairs
        # We are trying to find the minimum cost
        # And we can either start from index 1 and index2

        # [1,2,3]

        # 0 -> 1/2
        # 1 -> 2, 3
        # 2 -> 3
        # minimum cost

        # We can use recursion for each index we are going to go up the stirs and get the minimum cost of either choosing i +1 or i + 2
        memo = {}

        def dfs(i):
            if i >= len(cost):
                return 0
            
            if i in memo:
                return memo[i]
            
            minimum_cost = cost[i] + min(dfs(i + 1), dfs(i + 2))
            memo[i] = minimum_cost

            return minimum_cost
        
        return min(dfs(0), dfs(1))

        # Overlapping subproblems and since we have too chouces its going to have a time complexity of 2^n

        # space O(n)

        # We can use tabulation 
        # Rather than using recursion we can just use for loop from the top to bottom

        
        cost1 = 0
        cost2 = 0

        for i in range(2, n + 1):
            temp = cost1
            cost1 = min(cost2 + cost[i - 2], cost1 + cost[i - 1])
            cost2 = temp
            #dp[i] = min(dp[i - 2] + cost[i - 2], dp[i-1] + cost[i - 1])
        
        return cost1

