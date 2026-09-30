class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        def backtrack(index,current_sum):
            if current_sum == target:
                result.append(path.copy())
                return
            
            if current_sum > target:
                return
            
            for i in range(index, len(nums)):
                path.append(nums[i])

                backtrack(i, current_sum + nums[i])

                path.pop()

        backtrack(0,0)

        return result