class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        We can either take it or dont take the value
        We need to sort to ensure no duplicate subarrays
        If we dont we need to generate all combinations
        and use a set therefore the time complexity will be n.2^n
        """

        results = []
        path = []
        n = len(nums)
        nums.sort()
        def backtrack(start):
            results.append(path.copy())
            
            for end in range(start, n):
                if end > start and nums[end] == nums[end - 1]:
                    continue
                
                path.append(nums[end])
                backtrack(end + 1)
                path.pop()

        backtrack(0)
        return results