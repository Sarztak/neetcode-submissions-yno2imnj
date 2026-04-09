class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos = {}
        n = len(s)
        if n == 0:
            return 0
        max_len = 1
        i = j = 0

        while j < n:
            if s[j] in pos:
                # when I needs to jump to a new position everything before that needs to be decomissioned
                # that is from i to pos[s[j]] everything needs skipped over
                # otherwise I will be using stale position and I don't need i to be back to a previous position
                # if i is already greater than pos[s[j]] or the stale position then don't update
                if i <= pos[s[j]]:
                    i = pos[s[j]] + 1
                pos[s[j]] = j
            else:
                pos[s[j]] = j
            
            max_len = max(max_len, (j - i + 1))
            print(max_len, i, j)
            j += 1
        return max_len