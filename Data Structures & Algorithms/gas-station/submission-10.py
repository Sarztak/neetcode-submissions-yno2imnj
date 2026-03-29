class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        n = len(gas)
        for i in range(n):
            total = gas[i] - cost[i]
            if total < 0:
                continue
            j = (i + 1) % n
            while j != i:
                total += (gas[j] - cost[j])
                if total < 0:
                    break
                j = (j + 1) % n
            if j == i:
                return j
        return -1 
        