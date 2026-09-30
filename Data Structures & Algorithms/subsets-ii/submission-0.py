class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
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