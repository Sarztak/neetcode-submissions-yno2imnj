class Solution:
    def countSubstrings(self, s: str) -> int:
        L = len(s)
        dp = [[False] * L for _ in range(L)]

        # 1. Case l = 1
        for i in range(L):
            dp[i][i] = True
        
        # 2. Case l = 2
        for i in range(L - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True 

        # 3. Case l >= 3 
        for l in range(3, L + 1):
            # the max value for m is L - l for n <= L - 1
            for m in range(L - l + 1):
                n = m + l - 1
                dp[m][n] = dp[m + 1][n - 1] and (s[m] == s[n])

        # find the number of string that palindrom
        count = 0
        for m in range(L):
            for n in range(L):
                if dp[m][n]:
                    count += 1
        
        return count