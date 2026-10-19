class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # subset1 = [2,3] = 5
        # subset2 = [1,4] =5
        # return True
        
        # each subset should equal to the sum of the total// 2
        # Input: nums = [1,2,3,4,5]
        # sum 15 // 2 = 7.5 its impossible
        # So therefore we can just return False

        # Base case. If total % 2 == 0: return False

        # Can we have duplicate numbers
        # What is the minumum length of athe array
        # The length array is greater than 1 but less than 100

        # We know that is subset1 is equal to the half of total.
        # Then the other half is going to be equal to half of total as well
        # So we only need to solve for one subset and then we can return True
        # For each elemenet, we have 2 decisions which leads 2 different paths
        # Therefore the time complexityt is going to be O(2^n)
        
        # Space complexity is going to be O(1)
        # clearly at for example. We could come from either 2 or 1
        # Clearlyt tyhere is going ot be recurring subproblems
        # So what we can do is store a dictopnaru that cointains the value and the sum up to that elemenet

        total = sum(nums)

        if total % 2 != 0:
            return False
        memo = {}
        half = total // 2

        def dfs(i, amount):
            if amount == half:
                return True
            
            if i >= len(nums) or amount > half:
                return False
            
            if (i, amount) in memo:
                return memo[(i, amount)]
            
            take = dfs(i + 1, amount + nums[i])
            skip = dfs(i + 1, amount)

            memo[(i, amount)] = take or skip
            return take or skip
        
        return dfs(0,0)
            

