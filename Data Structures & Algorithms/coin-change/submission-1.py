class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # I am given a list of coins
        # I am given a target amount
        # you would like me to figure out the minimum amount of coins needed to make the target
        # I can use unlimited amount of coins
        # If there are no combination of coins that can make this amount then we just return -1

        # [1,5,10] amount = 12
        # 2 x 1 and 1 x10 = 12

        # [1,4,6] = ??

        # 12 - 11, 7,  2 -> 10, 6, 1, 
        # c^a

        # So were going to have an array of size amount os we can store the minimum
        # number of coins to make that amount
        
        # for every coinf we are going to see the minimum it took to make (i - coin)
        # where i >= coin

        dp = [float('inf')] * (amount + 1)

        dp[0] = 0

        for amount in range(1, amount + 1):
            for coin in coins:
                if amount >= coin:
                    dp[amount] = min(dp[amount], dp[amount - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1

