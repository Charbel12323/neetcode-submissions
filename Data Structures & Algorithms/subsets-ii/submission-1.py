class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # What makes a duplicate subset
        # First you can either take it or dont take it (boolean)
        # We need to sort
        # [1,1,2] = [1,1,2], [1,2], [1,2]
        # So for a duplicate when skipping, we need to check wheteher there is aduplicate element

        results = []
        path = []
        nums.sort()

        def backtrack(index):
            if index == len(nums):
                results.append(path.copy())
                return
            
            path.append(nums[index])
            backtrack(index + 1)

            path.pop()

            while index < len(nums) - 1 and nums[index] == nums[index + 1]:
                index += 1
            
            backtrack(index + 1)
        
        backtrack(0)
        return results
