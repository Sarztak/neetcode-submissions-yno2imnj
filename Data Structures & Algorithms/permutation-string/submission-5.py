import string
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # the logic is that there is a fixed window of length len(s1) under which the frequency of characters should be exactly equal
        # update one from the left as we move forward and update one from right which reducing frequency
        # there is a better way to avoid all the checking with every possible character in s1 but it will still work

        n1 = len(s1)
        n2 = len(s2)

        freq_s2 = {}
        freq_s1 = {}

        # setting up things
        # also for this problem there is no constraint on the length of s1 and s2 so they can be 
        # anything; in case n2 < n1 there is no possible solution

        if n2 < n1:
            return False

        for i in range(n1): # I didnt' read the condidtion carefully before and assumed that n1 <= n2 for all the cases.
            # if the key does not exists then get returns 0 and then 0 + 1 becomes the starting value
            freq_s1[s1[i]] = freq_s1.get(s1[i], 0) + 1 # default value 0 if not found
            freq_s2[s2[i]] = freq_s2.get(s2[i], 0) + 1

        # as we enter the loop the string is s2[i: j + 1] already so compare the frequency of character
        i, j = 0, n1 - 1
        while j < n2:
            # compare the frequency
            condition_met = True

            for k, v in freq_s1.items():
                if k not in freq_s2 or freq_s2[k] != v:
                    condition_met = False
                    break
            
            if condition_met:
                return True

            # now update the pointers and add the new frequecy 
            j += 1 # I cannot add new character until I update

            # also j can get out of index if j == n2 - 1   
            if j < n2:
                freq_s2[s2[j]] = freq_s2.get(s2[j], 0) + 1
            
            if s2[i] in freq_s2:
                freq_s2[s2[i]] = max(0, freq_s2[s2[i]] - 1) # keep the count at least 0 not less than that.

            i += 1 # I cannot update i before removing the old character 
        return False