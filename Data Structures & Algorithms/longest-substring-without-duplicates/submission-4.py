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
                # that is from i to pos[s[j]] everything needs to be deleted
                new_pos = pos[s[j]] + 1
                for k in range(i, pos[s[j]] + 1):
                    del pos[s[k]]
                i = new_pos
                pos[s[j]] = j
            else:
                pos[s[j]] = j
            
            max_len = max(max_len, (j - i + 1))
            print(pos, max_len, i, j)
            j += 1
        return max_len