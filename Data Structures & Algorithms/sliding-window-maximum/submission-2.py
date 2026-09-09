class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() # largest -> smallest
        results = []

        for right in range(len(nums)):

            while q and nums[q[-1]] < nums[right]:
                q.pop()
            
            q.append(right)

            if q[0] <= right - k:
                q.popleft()
            
            if right >= k - 1:
                results.append(nums[q[0]])
        
        return results