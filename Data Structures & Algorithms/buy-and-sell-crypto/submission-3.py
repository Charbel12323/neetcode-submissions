class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force
        # For each index, I'd go through all the ohter indexes seeing the max profit I can make
        # Time complexity would be O(n^2) while space is O(1)

        # Optimal solution
        # - We would like to buy at the cheapest price and sell at the highest
        # - We can start with the current index. If another index is cheaper we start from there and keep looping calculating the profit until we make the end

        max_profit = 0
        current = prices[0]
        for price in prices:
            if price < current:
                current = price
                continue
            max_profit = max(max_profit, price - current)
        
        return max_profit
            