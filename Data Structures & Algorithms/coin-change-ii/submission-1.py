class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for composite in range(coin, amount + 1):
                dp[composite] += dp[composite - coin]
        
        return dp[amount]