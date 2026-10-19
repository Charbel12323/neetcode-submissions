class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We need to return the minimum number k ti eat all banas within h hours
        # the maximum value of bananas u can eat would eb the max value in piles
        # the minimum value is going to be 1
        # 1 <= k <= max(piles)


        # How to caluclate the amount of hours
        
            
        left, right = 1, max(piles)
        min_eating_rate = float('inf')

        while left <= right:

            eating_rate = (left + right) // 2

            hours_taken = 0
            for i in range(len(piles)):
                current_pile = piles[i]

                hours_taken += math.ceil(current_pile / eating_rate)
                
            if hours_taken > h:
                left = eating_rate + 1
            else:
                min_eating_rate = min(min_eating_rate, eating_rate)
                right = eating_rate - 1
        
        return min_eating_rate if min_eating_rate != float('inf') else -1