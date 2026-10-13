class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Since the windows are overlapping
        # We are only ever removing 1 integer
        
        # That means we carry on the maximum from the previous window if its still in the second window

        # [1,2,1,0]
        # 2 = max
        # 1 = But could be the next macimum value for the overlapping sliding window
        # 0 same as well could be the maximum

        # descending values by there index
        # Why there index its to check if they ar estill part of the window

        # queue = FIFO we are going to keep order. And the time complexity will be O(1)


        # So left and right pointer
        # build the. sliding winow until size k
        # For every integer we see, if its greater than the maximum value, then we pop the whole queue and start again snice we know that the previous will value will no longer be the maximum,
        # If we find a smaller value than max, we add it to the queue since this could be the maximum for the next window

        # We must store the indexes, because we need to check if this current value is still within the window

        # Time Complexity = O(n)
        # Space Complexiy = O(k)

        # So for every value, we must check whether its greater than the current max in the queue or smaller. 
        # If smaller append it, if greater pop the whole queue and append it
        # To get the window size its going to be (right - left + 1)
        # So once the window size is > k then we can append the root of the queue to the result
        # 
        
        queue = deque()
        results = []
        left = 0

        for right in range(len(nums)):
            
            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop()
            
            queue.append(right)
            
            if (right - left + 1) == k:
                results.append(nums[queue[0]])
                left += 1

                if queue and queue[0] < left:
                    queue.popleft()
            

        
        return results




            

        
