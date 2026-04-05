class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        n_g = n // groupSize

        if n % groupSize != 0:
            return False # cannot partition hand into groupSize array and leave not elements

        hand = sorted(hand)
        groups = [[hand[0]]]

        # the general idea is that for each element make a decision either to place it an existing array or start a new array with that element as first one
        # if the size of anything else goes out of bound for any element then return false
        for i in range(1, n):
            has_a_group = False
            for g in groups:
                if 0 < len(g) < groupSize:
                    if g[-1] - hand[i] == -1: # have an increasing order of elements
                        g.append(hand[i])
                        has_a_group = True
                        break

            if not has_a_group:
                if len(groups) < n_g:
                    groups.append([hand[i]])
                else:
                    return False # if there are no more groups to fill then return false since there is no place 


        return True
        