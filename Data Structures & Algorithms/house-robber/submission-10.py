class Solution:
    def rob(self, nums: List[int]) -> int:
        # maximum amount of money we can rob
        # we cant rob 2 adjacent homes

        # Can the list be empty or do we always have 1 or more homes
        # Whats the maximum amount of homes we can have in the input

        # # reiterate
        # [1,1,2,3] -> Maximum cost? 4

        # Ok so for each home can either rob or dont rob
        # If we rob then we must get the i -2 home + the current price. If we dont rob this home, then we just get the prev max
        # We are going to start from the last home
        # Then from there we are going to calculate the maximum profit
        # maxProfit(i) = max(maxProfit(i-2) + current cost, maxProfit(i - 1))
        # Clearly we are solving repeated subproblems and since we have 2 choices for each index the time complexit will be O(2^n)
        # We can use memoization to cache the computed values with O(1) lookup however the space will be O(n) but time will be O(n) instead which is an improvement

        # so we are only using 2 variables
        # So instead of using recursion we can define the first 2 base cases
        # we start with 0
        # first home we use its current value
        # Then we update all the other homes
        # This would reduce the space to O(1) and time to O(n)

        if len(nums) == 1:
            return nums[0]
        
        prev1 = nums[0]
        prev2 = 0

        for home in range(1, len(nums)):
            temp = prev1
            prev1 = max(prev1, prev2 + nums[home])
            prev2 = temp
        
        return prev1