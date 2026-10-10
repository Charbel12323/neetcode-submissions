class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # So we can get the middle value
        # if the value is greater than nums[right] then we know the left side is sorted
        # if value > nums[left] then we know we can move the rigth pointer
        # Else we can move the left pointer

        # if the value is less than nums[right] then we know the right side is sorted
        # this means if we the current value and nums[right cause we know thats sorted]

        left, right = 0, len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] > nums[right]:
                if target >= nums[left] and target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else:
                if target <= nums[right] and target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1