class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Does the input contain negative values
        # Can the input be empty
        # Is there always a unique solution - No there isnt. Okay so then we return empty array
        # IF the array is all 0, woudl we just return the array

        # BRUTE FORCE SOLUTION:
        # I would use backtracking. For each index I'd either take or dont take the next index until the len(path) == 3. If the sum of the path is equal 0 then we append that triplet and pop. Since we dont want duplicate answers we must check on each recursion level whether the current element is equal to the previous one if so we need to skip it. To do that we also need to sort the array
    # Time complexity = N^3 and space 

    # Optimal solution
    # We can sort the array to ensure we skip duplicate starting triplets
    # And since we sorted the array, its going to be ascending order
    # Therefore we can use 3 pointers. One at the current index were on. 
    # One on the index after. And one on the index in the end
    # if all 3 add up and are greater than 0 we can move right
    # if they are less than 0 I can move the left pointer
    # if they are on 0 then we can append the values onto the array
    # if left is equal right then there is no solution so we start again with a new index. This would be O(n^2) cause for each index we are checking everythign on the right of it. SO O(n.nnlogn) = O(n^2logn)
    # [-4,-1,-1,0,1,2]


        results = []
        nums.sort()

        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                total_sum = nums[i] + nums[left] + nums[right]
                
                if total_sum < 0:
                    left += 1
                elif total_sum > 0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left -1]:
                        left += 1
            

        return results