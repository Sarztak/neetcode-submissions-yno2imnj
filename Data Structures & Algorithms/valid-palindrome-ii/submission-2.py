class Solution:
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        """
        Counting does not work here, the best solution is to just check if the 
        remaining strings are palidromes or not after a mismatch
        """
        def isPalindrome(s):
            i = 0
            j = len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return isPalindrome(s[i + 1:j + 1]) or isPalindrome(s[i:j])
        
        return True
