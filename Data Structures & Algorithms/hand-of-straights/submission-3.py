class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        unique = set(hand)
        maxInt = max(unique)
        freq = [0]*(maxInt + 1)
        for h in hand:
            freq[h] += 1
        
        while True:
            i = 0
            while freq[i] <= 0:
                i += 1
                continue
            lastHand = -1
            
            if len(freq) - i < groupSize:
                return False
            
            for _ in range(groupSize):
                       
                freq[i] -= 1
                if freq[i] < 0:
                    return False
                if lastHand == -1:
                    lastHand = i
                else:
                    if i - lastHand != 1:
                        return False
                    else:
                        lastHand = i
                i = i + 1
                   
            if all(freq[j] <= 0 for j in range(maxInt + 1)):
                break
        
        return True
        