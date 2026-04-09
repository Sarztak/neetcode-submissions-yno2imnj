class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        n = len(s)
        if n == 0:
            return 0
        max_len = 1
        i = j = 0
        """
        This problem is similar to duplicates 2 problem in that you again need to 
        do something where there is a duplicate element. The tricky part for me to understand
        was that the i can jump to any position less than j when there is a duplicate but not always 
        i needs to be updated; in case I is already greater than the previously stored position
        here I am using a dictionary which can store state position - those elements that are no longer 
        part of the window, but I don't remove them so I need to be careful not to use those stale positions
        this took me time to realize. 
        """
        while j < n:
            if s[j] in pos:
                # when I needs to jump to a new position everything before that needs to be decomissioned
                # that is from i to pos[s[j]] everything needs skipped over
                # otherwise I will be using stale position and I don't need i to be back to a previous position
                # if i is already greater than pos[s[j]] which is the stale position then don't update
                if i <= pos[s[j]]:
                    i = pos[s[j]] + 1
                pos[s[j]] = j
            else:
                pos[s[j]] = j
            
            max_len = max(max_len, (j - i + 1))
            j += 1
        return max_len