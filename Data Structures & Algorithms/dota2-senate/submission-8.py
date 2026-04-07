from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r, d = deque(), deque()
        n = len(senate)
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            if r[0] < d[0]: # who has the turn to vote Radiant or Dire
                d.popleft()
                x = r.popleft() + n
                r.append(x)
            else:
                r.popleft()
                x = d.popleft() + n
                d.append(x)
        
        return 'Radiant' if len(r) > 0 else 'Dire'