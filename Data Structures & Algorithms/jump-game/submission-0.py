class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest_jump = 0

        for i in range(len(nums)):
            if i > furthest_jump:
                return False
            
            furthest_jump = max(furthest_jump, i + nums[i])

            if furthest_jump >= len(nums) - 1:
                return True