class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [3,4,5,6,1,2] -> That descending spot is what we are looking for
        # [4,5,6] [1,2,3]
        
        left, right = 0, len(nums) - 1
        # We have 2 conditions
        # if nums[middle] > nums[right] -> left = middle + 1
        # if nums[middle] < nums[right] -> right = middle 
        # Once they are equal then that is our minimum value

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle
        
        return nums[left]