class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # im given an interger array heights, you would want me to return the maximum amount of water that the container can store

        # Can the input containe one heught or is the minimum 2
        # Can a hieght be 0?
        # You would like me to return the maximum area

        # Brute force solution
        # Fpr each height I would compare with all the other heights, calculate area and check if it is the max. This is O(n^2) solution with O(1) space

        # Optimal solution.
        # Since the width can be calculated using the indexes, we can have 2 pointers one on  the left and one on the right
        # Our right height is our pillar since the width matters the most
        # so if right - 1 is less than move left. if left + 1 is less than right - 1 we must move the right one

        # This is going to be an O(n) solution

        left, right = 0, len(heights) - 1

        max_area = 0

        while left < right:
            width = right - left
            min_height = min(heights[left], heights[right])
            max_area = max(max_area, width * min_height)

            if heights[right] >= heights[left]:
                left += 1
            else:
                right -= 1
        
        return max_area
            
