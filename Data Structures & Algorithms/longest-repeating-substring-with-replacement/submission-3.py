from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charDict = defaultdict(int)
        max_length = 0
        l = 0
        curr_max_len = 0
        for r in range(len(s)):
            charDict[s[r]] += 1
            curr_max_len = max(curr_max_len, charDict[s[r]])
            while (r - l + 1) - curr_max_len > k:
                charDict[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        
        return max_length
            
        