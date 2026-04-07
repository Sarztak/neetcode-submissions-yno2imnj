from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r = deque()        
        d = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                r.append(i)
            else:
                d.append(i)

        while r and d:
            for i in range(len(senate)):
                print(r, d)
                if i in r:
                    # declare victory 
                    if len(r) > len(d):
                        return 'Radiant'
                    
                    # ban the first available member
                    d.popleft()

                    # also the person who voted goes back in line to vote again
                    x = r.popleft()
                    r.append(x)

                elif i in d:
                    # declare victory:
                    if len(d) > len(r):
                        return 'Dire'
                    
                    # ban the first available memeber
                    r.popleft()

                    # person who voted goes back to vote again
                    x = d.popleft()
                    d.append(x)
                else:
                    continue

        if len(r) > 0:
            return 'Radiant'
        else:
            return 'Dire'