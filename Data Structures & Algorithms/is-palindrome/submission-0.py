class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = ""
        for a in s:
            if a.isalnum():
                t = t + a.lower()
        return t == t[::-1]
        