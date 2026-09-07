from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Ok so we know if we eat a certain k then everything after that is useless
        # K can either be 1 to greatest value in the array
        
        left, right = 1, max(piles)

        min_k = float('inf')

        while left <= right:
            k = (left + right) // 2
            hours_taken = 0

            for p in piles:
                hours_taken += ceil(p/k)
            
            if hours_taken <= h:
                min_k = min(min_k, k)
                right = k - 1
            else:
                left = k + 1
            
        return min_k
