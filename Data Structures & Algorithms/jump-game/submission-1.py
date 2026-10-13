class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_index = 0

        for i in range(len(nums)):
            if i > furthest_index:
                return False
            
            furthest_index = max(furthest_index, i + nums[i])
            if furthest_index >= len(nums) - 1:
                return True
        