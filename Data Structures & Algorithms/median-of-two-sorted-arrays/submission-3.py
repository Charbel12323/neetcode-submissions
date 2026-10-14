class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # arrays are sorted
        # Return the median of all the elements
        # Median is the middle value

        # Can nums 1 or nums 2 be empty?. Yes!
        # Are there negative values

        # [1,3].  [2,4]

        # Median?
        # 1,2,3,4 =. (2 + 3) // 2
        
        # odd [1,2] [3]
        # median is just 2
        # My brute force approach:
        # Iterate through both arrays
        # sotre them in a new arrau
        # sort them
        # And then use binary search to get the median

        # If we split up each array to a left and right section
        # Where left is smaller than right
        # Then all we would have to do is get the greatest left value and smallest right value to calculate the median if even
        # Get the greatest left value if odd

        # How are we going to split these sections
        # [1,2,3,4]
        # We would need to calculate the length of the array
        # And then split it so that len(left) == len(right) or len(right) - len(left) > 1

        # We can use binary search to figure out where the split is going to be
        # We should also do it with the smaller array since we can get an out of index bounds

        # So we did binary search and figure where the split is going to be
        # Then once we figure that out
        # We can then calculate where the second array split is goingt o be by 
        # doing total - parition1 which is where the second half will be
        # when we split the total length by 2 we knnow how much will be left and how much will be on the right
        # Then we do binary search, the first array will contain a split. Then we can do half - this index split that we found
        # So now we know how mant are on the left

        # We can get the sum of the left and sum of the right and compare
        # If difference is greater than 1 then we know we have to move the right pointer closer to reduce the left size if not then we can move it left 
        # Since its sorted the greates value on the left side in nums2 has to be less than the ending for nums 1
        # and same goes vice versa
        # thats the condition that allows us to switch
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2 # Represents how many values on the left side
        left = 0
        right = len(nums1)

        while left <= right:

            partition1 = (left + right) // 2
            partition2 = half - partition1

            # Know we know how many values are on the left of both arrays
            left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            right1 = nums1[partition1] if partition1 < len(nums1) else float('inf')
            left2 = nums2[partition2 - 1] if partition2 > 0 else float('-inf')
            right2 = nums2[partition2] if partition2 < len(nums2) else float('inf')


            if left1 > right2:
                right = partition1 - 1

            elif left2 > right1:
                left = partition1 + 1
            else:
                if (total % 2) == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1,left2)




        