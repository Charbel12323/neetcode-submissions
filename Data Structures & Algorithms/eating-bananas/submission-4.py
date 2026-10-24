import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        minimum_k = float('inf')

        while left <= right:
            eating_hour = (left + right) // 2

            hours_taken = 0

            for pile in piles:
                hours_taken += math.ceil(pile / eating_hour)

            if hours_taken <= h:
                minimum_k = min(minimum_k, eating_hour)
                right = eating_hour - 1
            else:
                left = eating_hour + 1

        return minimum_k