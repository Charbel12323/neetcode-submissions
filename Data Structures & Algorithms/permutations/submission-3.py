class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        path = []
        used = set()

        def backtrack():
            if len(path) == len(nums):
                results.append(path.copy())
                return

            for num in nums:
                if num in used:
                    continue

                path.append(num)
                used.add(num)

                backtrack()

                path.pop()
                used.remove(num)

        backtrack()  # Missing line
        return results