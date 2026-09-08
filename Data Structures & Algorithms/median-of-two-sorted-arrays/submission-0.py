class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # We want to binary search on the shorter array for better optimization
        # lets assume we have nums1 = [1,3] and nums2 = [2,4]
        # We need to split both arrays into sections. Left and Right
        # 1 | 3     2 | 4
        # We have 4 elements that means we need 2 on the left side and 2 on the right side. When doing binary search on the smaller array we get 1 | 2. 
        # To figure out how many elements we need for the array on th eleft side we must do (m + n + 1) // 2 - (Amount on the left side)
        # Once we get that we have 2 left sides and 2 right sides. The left side must always be smaller than the right side therefore left1 < right2 and left2 < right1
        # If it is then the mediam is very easy to find
        # If it isnt then we did some miss calculation and we must move right to where the partititon was -1
        # if left1 < right2 we took many elements from num1 so we need to move the partition
        # if its the opposite then we need to take more elemnts

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m ,n = len(nums1), len(nums2)
        left, right = 0, m
        half = (m + n + 1) // 2

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = half - partition1

            left1 = nums1[partition1 - 1] if partition1 > 0 else float('-inf')
            right1 = nums1[partition1] if partition1 < m else float('inf')

            left2 = nums2[partition2 -1] if partition2> 0 else float('-inf')
            right2 = nums2[partition2] if partition2 < n else float('inf')

            if left1 <= right2 and left2 <= right1:

                if(m + n) % 2 == 1:
                    return(max(left1, left2))
                
                return (max(left1,left2) + min(right1,right2)) /2
            
            elif left1 > right2:
                right = partition1 - 1
            else:
                left = partition1 + 1