class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        path = []
        candidates.sort()

        def backtrack(start, current_sum):
            if current_sum == target:
                results.append(path.copy())
                return
            
            if current_sum > target:
                return
            
            for end in range(start, len(candidates)):
                if end > start and candidates[end] == candidates[end-1]:
                    continue
                
                path.append(candidates[end])
                backtrack(end + 1, current_sum + candidates[end])
                path.pop()
        
        backtrack(0,0)
        return results


