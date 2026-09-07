class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # What is the best solution
        # Finding a consecutive element we need to start from a maximum value and subtract 1 if it exists we increment else we find the next max value

        nums_set = set(nums)
        max_consecutive = 0
        
        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                length = 1
                while current + 1 in nums_set:
                    length += 1
                    current += 1
                
                max_consecutive = max(max_consecutive, length)
        
        return max_consecutive
