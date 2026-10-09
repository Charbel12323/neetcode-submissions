import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # I am given an integer array piles where each index represents the number of bananas. I am also given h which represnt the number of hours i have to eat all the banans. I need to pick the minimum number of hours to eat all the bananas in the pile. Cant eat from another pile if finished from the current pile u must wait.

        # IM assuming the pile can be from 1 <= piles[i] < 100000
        # same goes for the length.
        # Are we always guaranteed a solution. if h is way to small, what should I return

        # Ok so we know that the maximum value of k is going to be the maximum value in piles. [1,4,3,2] maxK = 4
        # So now we know we can start from the maximum value and decrement if we can still go. The last one that cant go is our minimum value. 
        # Brute force solution
        # I'd get the maximum value from teh pile. then i'd try to eat everything in the array. If it is less than h. Then we can decrement the max vlaue by one and try again. # O(n) solution. proably of O(n^2)

        # Optimal solution
        # We can use binary search. This is optimal because we know the eatring rate
        # can be from 1 .... max(piles)
        # So now we can get the middle try it, if it works we can decrease by moving right one down so it becmoes 3 for example. When ever it fails
            
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
        





