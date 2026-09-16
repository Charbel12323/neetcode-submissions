class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        # We either add or pop the stack
        # When do we add:
        # We have every temp, rather than having 2 for loops we can use 1 for loop
        # We keep checking if the current temp > original temp. If not add it
        # Then retreive the length when it passes and append to results
        # But then how do you go to the next temperature and start from there?

        stack = []
        results = [0] * ( len(temperatures))

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_index =stack.pop()
                results[prev_index] = i - prev_index
            
            stack.append(i)
        
        return results