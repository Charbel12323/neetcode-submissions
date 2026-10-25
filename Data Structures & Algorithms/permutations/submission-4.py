class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Return all possible permutations. Any order
        What is permutation - A combinations of all the values

        nums = [1,2,3]

        [1,3,2] -> How do we do this
        FOr each element we can either take it dont take it. The depends if we have seen this element so far

        So for each recursion level we check if the element is in seen if it is we skip it

        What is the brute force solution?
        try every possible combinatoin remove duplicate n.2^n


        For each element we can take it or dont take it depending on what has already been seen
        n.2^n
        """


        results = []
        path = []
        seen = set()
        n = len(nums)
        def backtrack():
            if len(path) == n:
                results.append(path.copy())
                return
            
            for num in nums:
                if num in seen:
                    continue
                
                seen.add(num)
                path.append(num)
                backtrack()
                path.pop()
                seen.remove(num)
        
        backtrack()
        return results