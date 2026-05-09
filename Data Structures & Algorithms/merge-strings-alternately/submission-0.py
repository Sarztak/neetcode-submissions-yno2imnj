class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)
        i = 0
        j = 0
        k = 0
        s = ""
        while i <= n - 1 and j <= m - 1:
            if k % 2 == 0:
                s += word1[i]    
                i += 1
            else:
                s += word2[j]
                j += 1
            
            k += 1
        
        if i == n:
            s += word2[j:]
        elif j == m:
            s += word1[i:]
        
        return s