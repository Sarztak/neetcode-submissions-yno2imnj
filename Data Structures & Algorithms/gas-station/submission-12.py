class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        for i in range(n):
            gas_in_tank = 0
            can_complete = True
            for j in range(n):
                if cost[(i + j) % n] > gas_in_tank + gas[(i + j) % n]:
                    can_complete = False
                    break
                gas_in_tank -= (cost[(i + j) % n] - gas[(i + j) % n])
            
            if can_complete:
                return i
        
        return -1
                