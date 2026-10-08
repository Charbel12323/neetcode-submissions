class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # You can either buy
        # You can either hold
        # You can either not buy and hold
        # You can either sell
        # You can only sell if bought
        # Can;t sell if u have nothing

        hold = float('-inf')
        sold = 0
        rest = 0

        for price in prices:
            prev_sold = sold
            prev_hold = hold
            hold = max(hold, rest - price) # Either hold or buy
            sold = prev_hold + price # selling
            rest = max(rest, prev_sold) # Money if just resting or if selling
        
        return max(rest, sold)
