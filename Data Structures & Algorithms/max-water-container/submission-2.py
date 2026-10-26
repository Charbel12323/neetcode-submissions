class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        Return the maximum amount of water 
        Area = width x height
        We need the greatest height and the greatest width
        Brtue force for each height we can traverse through all the othe rheights ahead of it and calculate the area. Do the same for all other heights until we have processed all of htem and return the maximum

        Better optoin - two pointers
        Use 2 pointers one on the right and one the left
        We calculate the area of each pointer and if which ever side is smaller we increment that until they are both equal to each other
        """

        left = 0
        right = len(heights) - 1

        max_area = 0
        while left < right:
            height = min(heights[left], heights[right])
            width = (right - left )

            area = (height * width)
            max_area = max(max_area, area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
