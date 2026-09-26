class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        total_gas, total_cost = sum(gas), sum(cost)

        if total_gas < total_cost:
            return -1
        
        gas_tank = 0
        winning_station = 0

        for i in range(len(gas)):
            gas_tank += (gas[i] - cost[i])

            if gas_tank < 0:
                winning_station = i + 1
                gas_tank = 0
        
        return winning_station
            
