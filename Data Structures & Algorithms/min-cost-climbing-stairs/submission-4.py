class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Return minimum cost to make it to the stop of stairs
        # We know the cost to start from 0 and the cost to start from 1 start at 0
        # For each step, we can either go one step or 2 steps

        # [1,2,3] # step3 = (Minimum cost from step1 + cost, minimum cost from step2 + cost)
        # We would like to reach the top of the stair case which is len(cost) + 1
        # Can the length of the array be less than or equal to 2
        # If so are we just going to return 0
        # What is the maximum length of the array - checking for recursion limit
        
        # I'd start start from the top floor and tehn recursivelt check the min cost for the step before or the step before 
        # We would want the minimum of this
        # MinCost(i) = min(MinCost(i-1) + cost[i-1], MinCost(i-2) + cost[i-2]
        # Since we have 2 choices for each step, this is going to be a 2^n time complexity
        # Clearly we are going to have overlapping subproblems
        # We can use memoization to ensure that the time complexity is O(1) but then the space will be O(n)

        # Clearly we only require the previous 2 results so rather than storing all the information we can start from the first 2 base cases and iteractively go upwards
        # This would make the time complexity O(n) and space O(1)

        # --- Time to code

        # Our bases cases is that both first steps cost 0
        # So then we can start at index 2 or step 3
        
        prev1 = 0
        prev2 = 0


        for i in range(2, len(cost) + 1):
            temp = prev1
            prev1 = min((prev1 + cost[i - 1]), (prev2 + cost[i - 2]))
            prev2 = temp
        
        return prev1

        # Dry run
        # Lets start with 2 elemenets 
