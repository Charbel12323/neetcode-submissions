class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # A permutation is all the ways the array can be re ordered
        # A permitations is when len(path) == len(nums)
        # example: [1,2,3]
        # We need all combinations so for each element in the array
        # We can pick any of the other ones
        # [1,2,3] [1,3,2] [2,1,3][2,3,1] [3,2,1][3,1,2]
        # We need ot ensure we can keep track of which index is being used
        # Why? Because it allow sus to skip that index

        used = set()
        results = []
        path = []

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
                