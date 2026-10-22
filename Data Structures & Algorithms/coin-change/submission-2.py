class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for amount in range(1, amount + 1):
            for coin in coins:
                if amount >= coin:
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1