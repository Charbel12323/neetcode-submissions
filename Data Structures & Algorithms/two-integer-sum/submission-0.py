class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # value -> index

        for i, num in enumerate(nums):
            composite = target - num
            if composite in seen:
                return [seen[composite], i]
            
            seen[num] = i