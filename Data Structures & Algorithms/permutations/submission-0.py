class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                results.append(path.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                
                path.append(nums[i])
                used.add(nums[i])

                backtrack()

                path.pop()
                used.remove(nums[i])
        

        backtrack()
        return results