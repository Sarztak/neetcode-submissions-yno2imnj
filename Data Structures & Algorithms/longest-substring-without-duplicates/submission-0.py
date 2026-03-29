class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        max_length = 0
        l = 0

        for r in range(len(s)):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            
            unique.add(s[r])
            max_length = max(max_length, r - l + 1)
     
        return max_length