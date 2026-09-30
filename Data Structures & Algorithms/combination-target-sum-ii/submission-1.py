class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []
        path = []
        candidates.sort()
        def backtrack(index, current_sum):
            if current_sum == target:
                results.append(path.copy())
                return
            
            if current_sum > target:
                return
            
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                
                path.append(candidates[i])

                backtrack(i + 1, current_sum + candidates[i])

                path.pop()
            
        backtrack(0,0)
        return results