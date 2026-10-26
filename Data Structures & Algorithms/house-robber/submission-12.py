class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev1 = nums[0]
        prev2 = 0

        for home in range(1, len(nums)):
            temp = prev1
            prev1 = max(prev1, prev2 + nums[home])
            prev2 = temp
        
        return prev1