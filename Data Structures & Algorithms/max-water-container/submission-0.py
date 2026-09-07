class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        left, right = 0, len(heights) - 1

        while left < right:
            length = right  - left
            height = min(heights[left], heights[right])

            max_area = max(max_area, length * height)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area