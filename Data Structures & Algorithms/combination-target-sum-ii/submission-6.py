class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """

        Return a list of unique combinations of candidates where the sum is going to be target

        We want unqique combinations
        We have duplicates in the array

        Solution1) We can use recursion
        For each element, we can either take it or dont take it. 
        Each element has multiple different choices
        So therefore we can use backtracking
        Our base case is going to be if the sum is equal to target
        Our edge case is if its greater than target
        We iterate through candidates
            - Issue is we have duplicates
        
        """
        results = []
        path = []
        candidates.sort()
        def backtrack(start, path_sum):

            if path_sum == target:
                results.append(path.copy())
                return
            
            if path_sum > target:
                return
            
            for end in range(start, len(candidates)):
                if end > start and candidates[end] == candidates[end - 1]:
                    continue
                path.append(candidates[end])
                backtrack(end + 1, path_sum + candidates[end])
                path.pop()
        
        backtrack(0,0)
        return results