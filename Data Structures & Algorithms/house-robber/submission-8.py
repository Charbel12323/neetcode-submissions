class Solution:
    def rob(self, nums: List[int]) -> int:
        # Can trob two adjacent homes
        # Return the maximum amount of money without alerting the police
        # [1,1,3,2]
        # 4
        # There can't be negative values
        # Whats the minimum length of the input? 1
        # [1,1,3,2]
        # For each house we are making a descision.
        # 1) rob this house and skip the other house
        # 2) Dont rob this house and wait for the next one
        # These descisions are influenced by the maximum profit you can make

        # 3 -> profit of 1 or or the current cost
        # 3 -> profit of 2 or the current cost
        # profit of 2 -> consists of either profit1 or current cost of 2
        # So clearly there is a recursion pattern

        # for each index we will check
        # maxProf(i) = maxProfit(i - 2) + cost, maxProfit(i - 1)

        # [1,3,4] profit = 0 for day 0 and we know the max profit of robbing the first home will be cost[i]

        # so now for 3. Its either 0 + 3, or 1 which would give us 3 5

        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]

        for house in range(2, len(nums) + 1):
            dp[house] = max(dp[house-2] + nums[house - 1], dp[house - 1])
        
        return dp[len(nums)]
