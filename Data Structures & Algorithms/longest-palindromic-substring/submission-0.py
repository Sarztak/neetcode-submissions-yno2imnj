class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # check for edge case first
        if n == 0:
            return ""

        # initialize start and end to track length
        start = end = 0

        # we expand from the center by considering each position as center
        for i in range(n):
            #length for odd length palidroms
            len1 = self.expand_around_center(s, i, i)

            # check for even length palindroms
            len2 = self.expand_around_center(s, i, i + 1)

            maxLen = max(len1, len2)

            if maxLen > end - start:
                start = i - (maxLen - 1) // 2 
                end = i + maxLen // 2

        return s[start:end + 1]

    def expand_around_center(self, s, start, end):
        while start >= 0 and (end <= len(s) - 1 ) and s[start] == s[end]:
            start -= 1
            end += 1
        return end - start - 1

            