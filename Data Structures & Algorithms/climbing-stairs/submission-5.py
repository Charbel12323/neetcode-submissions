class Solution:
    def climbStairs(self, n: int) -> int:
        # Number of distinct ways to climb the stairs
        # n = 3 : 1,1,1 , 1,2 , 2,1  = 3

        # n = 3. From each step we can either go 1 or 2 
        # To get to step 3. I could have either came from step 1 or from step 2
        # Im looking for the number of disctinct ways
        # I'd need the number of distinct ways from step and number of discting way from step 2
        # Only issue with this solution is that if we just use recursion, we will be overlapping subproblemns. 
        # Therefore the time complexity 2^n

        # NumOfWays to get to step 3 will be = NW(1) + NW(2)
        # We can use a cache to store the recomputed values so then the time complexity becomes O(1)
        # Since we are only reslying on the previous 2 steps. We can use an iterative approach starting from teh base cases so then we can ensure space(O(1))

        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        prev1 = 2 # Number of ways to make it to step 2
        prev2 = 1 # Number of ways to make it to step 1

        for step in range(3, n + 1):

            temp = prev1
            prev1 = prev1 + prev2 #3
            prev2 = temp # 2
        
        return prev1

        # Time compelxity will be O(n) and the space complexity will be O(1)
        # Test cases - dry run

        # 1
