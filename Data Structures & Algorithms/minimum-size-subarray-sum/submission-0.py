class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        min_length = float('inf')
        total_sum = 0
        for right in range(len(nums)): # O(n)
            total_sum += nums[right]
            
            while total_sum >= target: # Since were moving left pointers only forward O(1)
                length = (right - left + 1)
                min_length = min(min_length, length)
                
                total_sum -= nums[left]
                left += 1
        
        return min_length if min_length != float('inf') else 0