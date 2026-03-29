class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False # because I can't get equal partitions of size groupSize

        # sort the hand and check if we can get the groups of groupSize
        # in increasing order
        hand.sort()

        # get the count of each value
        count = Counter(hand)

        for num in hand: 
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True
        