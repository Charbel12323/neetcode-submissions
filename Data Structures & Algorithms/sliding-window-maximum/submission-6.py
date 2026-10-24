class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Return a list that contains the maximum of each sliding window

        """
        Brute force solution - For each element I'd iterate until the window size and use the max function to retrieve the maximum.
        Time complexity is going to be O(n^2)

        Better solution
        We know windows are overlapping by one so the previous maximum could be the maximum fo the current window

        We could use a monotonic deque to keep track of the largest maximum
        We store its index to ensure we can check if that maximum value is still part of the window
        If we find a value greater we are going to keep popping until we can find it some place to add
        So now for each window if the current maximum is in the window size we know its the maximum and we can use that. If its not then we know when we pop the next vlaue wil be the maximum
        """

        # Can k be greater than the input or can we assume k is always a valid number in respective to the input

        # If the input has a length of 1 then k is going ot have thje length of 1 correct/

        # Im assuming we are always guaranteed a solution


        queue = deque()
        results = []
        left = 0
        for right, num in enumerate(nums):

            while queue and num > nums[queue[-1]]:
                queue.pop()
            
            queue.append(right)
            
            if (right - left + 1) == k:
                results.append(nums[queue[0]])
                left += 1
                if queue[0] < left:
                    queue.popleft()

        return results

