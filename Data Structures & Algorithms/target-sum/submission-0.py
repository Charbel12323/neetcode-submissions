class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}  # sum -> number of ways

        for num in nums:
            next_dp = {}

            for total, ways in dp.items():
                add = total + num
                subtract = total - num

                next_dp[add] = next_dp.get(add, 0) + ways
                next_dp[subtract] = next_dp.get(subtract, 0) + ways

            dp = next_dp

        return dp.get(target, 0)