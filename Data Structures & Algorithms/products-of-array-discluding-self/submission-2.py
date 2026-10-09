class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # can the array be empty
        # Can there be negative numbers
        # Can there be 0 in the input
        # Is the answer guaranteed to fit a 32 bit integer
        
    
        # For the brute force method for each index I would calculate the product of the full array using 2 for loops  and then I'd divide by the current index we started on. This would be O(n^2). Space would be O(n).

        # Rather than that, we could use the prefix and suffix of each index to calculate the product.
        
        # length of 2 -> [1,2] return the inverse of the array
        # prefix = [1,1,2,8]
        # suffix = [48,24,6,1]

        # So we can build a prefix and suffix array where the prefix[0] and suffix[-1] must be 1s to ensure we dont multiply everythign by zero

        if len(nums) == 2:
            return [nums[1], nums[0]]
        
        prefix = [1] * (len(nums)) # [1,1,1,1] O(n)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        suffix = [1] * (len(nums)) # O(n)
        for j in range(len(nums) - 2, -1,-1): # O(n)
            suffix[j] = suffix[j + 1] * nums[j + 1]
        
        results = [(prefix[i] * suffix[i]) for i in range(len(nums))]
        
        return results