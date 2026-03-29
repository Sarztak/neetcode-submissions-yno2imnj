class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""

        countT, window = {}, {}
        left = 0
        l, right = 0, 0
        resLen = float('infinity')
        res = [-1, -1] 
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                a = s[l]      
                window[a] -= 1      
                if a in countT and window[a] < countT[a]:
                    have -= 1
                l += 1
        
        l, r = res
        return s[l: r + 1] if resLen != float('infinity') else ""
        