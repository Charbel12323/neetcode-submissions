class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Rotated
        # We have 2 different sections. A larger sorted section
        # A small sorted section
        # We are given a target
        # We need to find the target
        # Return -1 if it isnt found

        """
        nums = [3,4,5,6,1,2], target = 5

        We can us ebinary search since its sorted
        We first care about the section

        So when we make it at 4 for example we first need to see which sections its in
        Lets check with the right value if it is greater we are in another section
        Then once thats done we can then check if the target lays between the left value upto the middle. I fit \





        """


        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[middle] > nums[right]: # We are on the left section
                if nums[left] <= target < nums[middle]:
                    right = middle - 1
                else:
                    left = middle + 1
            else: # We are on the right section
                if target <= nums[right] and target > nums[middle]:
                    left = middle + 1
                else:
                    right = middle - 1
        
        return -1 
