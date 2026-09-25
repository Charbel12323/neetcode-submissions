class Solution:
    def jump(self, nums: List[int]) -> int:
        furthest_jump = 0
        jumps = 0
        current_end = 0

        for i in range(len(nums) - 1):
            furthest_jump = max(furthest_jump, nums[i] + i)

            if i == current_end:
                jumps += 1
                current_end = furthest_jump
        
        return jumps