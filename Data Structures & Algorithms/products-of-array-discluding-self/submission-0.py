class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # We have the prefix and we have the suffix
        # Prefix x Suffix = product except itself

        # First thing we need to do is get all the prefixes and suffixes

        result = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result
