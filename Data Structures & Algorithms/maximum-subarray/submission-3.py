class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Ok the array isnt sorted
        # THere are negative values

        """
        Find the subarray with the largest sum
        Solution1) Brute force solution
        For each element build all the sub arrays and get the maximum and do the same for all other elements
        O(n^2)

        Solution2) Better solution
        We can either take or dont take

        for each element we can either continue our subarray, or start new


        """
        current_sum = nums[0]
        max_subarray = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_subarray = max(max_subarray, current_sum)
        
        return max_subarray

            
            

            