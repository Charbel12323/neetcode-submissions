class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_product = nums[0]
        min_product = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            
            prev_max = max_product
            prev_min = min_product

            max_product = max(nums[i], prev_max * nums[i], prev_min * nums[i])
            min_product = min(nums[i], prev_min * nums[i], prev_max * nums[i])

            result = max(result, max_product)
        
        return result