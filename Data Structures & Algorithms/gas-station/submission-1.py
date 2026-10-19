class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If the total cost is greater than the total cost. Then we can retunr -1 since its impossible

        # gas = [1,2,3,4], cost = [2,2,4,1]
        # So for each station we can try to loop clockwise
        # If it fails, then we know the starting point will be anypoint after the failing point
        # By fail, I mean gas < 0



        total_gas = sum(gas)
        total_cost = sum(cost)

        if total_cost > total_gas:
            return -1
        
        winning_station = 0
        running_gas = 0

        for i in range(len(gas)):
            running_gas += gas[i] - cost[i]

            if running_gas < 0:
                winning_station = i + 1
                running_gas = 0
            
        return winning_station
