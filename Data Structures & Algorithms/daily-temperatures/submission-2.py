class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Return an array results where each element represnts the number of days after the ith day where a warmer temperature arises

        """
        temperatures = [30,38,30,36,35,40,28]
        results = [1,4,1,2,0,0]


        - Is the array sorted?
        - Can the temperatures be negative
        - Are there any duplicate temperatures
        
        - If there are no solutions then we just return an array of 0s

        Solution1 - For each temperature, iteratre through all other temperatures after the starting temp, and keep going until you find a greater temp. Once we do, find the difference between the end and start pointer and put that in the results. Time Complexity O(n^2) since we are iterating through each element more than once

        Solution2 - results is going to be length of len(temperatures) - 1
        Each index represnts the temperature.

        For each temperature, add the index to the stack. If the next temperature is less than current then we increment the results value using the index by 1 and add the new temp to the stack. We do the same thing until we find a temperature that is greater. 
        """

        results = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                index = stack.pop()
                length = (i - index)
                results[index] = length
            
            stack.append(i)
        
        return results


