class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        For each index i we can jump up to i + j
        We want the minimum number of jumps
        We can keep track of our fursthest jump for each element
        until we reach i + num
        Then we increment the jump by 1 
        """

        furthest_index = 0
        count = 0 
        current_index = 0

        for i in range(len(nums) - 1):
            furthest_index = max(furthest_index, i + nums[i])

            if i == current_index:
                count += 1
                current_index = furthest_index
        
        return count