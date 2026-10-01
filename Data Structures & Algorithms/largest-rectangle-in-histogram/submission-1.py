class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack holds the index and the height of all valid heights
        # As as the height is < height + 1 we are good

        max_area = 0
        stack = []

        for i, height in enumerate(heights):

            start = i

            while stack and height < stack[-1][1] :
                old_index, old_height = stack.pop()

                width = i - old_index
                area = old_height * width
                max_area = max(max_area, area)

                start = old_index
            
            stack.append((start,height))

        for i, height in stack:
            width = len(heights) - i
            area = width * height
            max_area = max(max_area, area)


        return max_area




