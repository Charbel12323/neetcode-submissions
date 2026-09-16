class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # A car fleet could eithe be one car individually or multiple cars together
        # A car fleet could occur if they reach the same destination at the same time even if its the target
        
        # target = 10 positions = [1,4] and speed = [3,2]
        
        # We could use a stack to track the current position of each vehivle
        # Time = distance/speed 
        cars = list(zip(position,speed))
        cars.sort(reverse=True) # We are sorting the cars my closest 

        stack = []

        for pst, spd in cars:
            time = (target-pst) / spd

            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)