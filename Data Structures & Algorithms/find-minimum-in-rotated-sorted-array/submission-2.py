class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2]
        # [3,4,5,6] [1,2] 

        # We can get the middle value using binary search
        # And we can check if that value is > the right side
        # If it is then we know the left side is sorted, therefore we can do left = middle + 1

        # If the value is less than the right side, we can move the right pointer to middle

        left,right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        
        return nums[left]