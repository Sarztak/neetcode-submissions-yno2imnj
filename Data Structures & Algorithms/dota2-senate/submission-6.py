from collections import deque
from heapq import heapify, heappop, heappush

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = [], []
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        heapify(r)
        heapify(d)

        while r and d:
            if r[0] < d[0]: # who has the turn to vote Radiant or Dire
                heappop(d)
                x = heappop(r)
                heappush(r, x + n)
            else:
                heappop(r)
                x = heappop(d)
                heappush(d, x + n)
        
        return 'Radiant' if len(r) > 0 else 'Dire'