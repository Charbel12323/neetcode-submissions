class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # So we know if target == 0 we found a sum
        memo = {}
        def backtrack(amount):
            if amount == 0:
                return 1

            if amount in memo:
                return memo[amount]            
            count = 0
            for n in nums:
                if n <= amount:
                    count += backtrack(amount - n)
            
            memo[amount] = count
            return count
        
        return backtrack(target)