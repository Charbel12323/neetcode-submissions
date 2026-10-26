class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        We can either rob a house or skip a house
        dp[i] = (dp[i-2] + nums[i], dp[i - 1])


        """
        memo = {}

        def dfs(i):
            if i < 0:
                return 0
            
            if i in memo:
                return memo[i]
            
            rob = dfs(i - 2) + nums[i]
            skip = dfs(i - 1)

            memo[i] = max(rob,skip)

            return max(rob,skip)
        
        return dfs(len(nums) - 1)