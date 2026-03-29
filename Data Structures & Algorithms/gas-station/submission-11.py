class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        for i in range(n):
            start = i; tank = 0; visited = [False]*n
            for j in range(start, 2 * n):
                j = j % n
                if visited[j]:
                    return start
                if gas[j] + tank < cost[j]:
                    break
                else:
                    tank += gas[j] - cost[j]
                    visited[j] = True
        return -1        