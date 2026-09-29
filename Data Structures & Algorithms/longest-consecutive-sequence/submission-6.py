class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)

        max_sequence = 0

        for num in nums_set:
            
            if num - 1 not in nums_set:
                count = 1
                while (num + 1) in nums_set:
                    count += 1
                    num = num + 1
            
                max_sequence = max(max_sequence, count)
        
        return max_sequence
