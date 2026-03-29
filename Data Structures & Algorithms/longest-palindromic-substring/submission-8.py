class Solution:
    def longestPalindrome(self, s: str) -> str:
        L = len(s)
        dp = [[False] * L for _ in range(L)]

        for i in range(L):
            # each string of length one is a palindrome
            dp[i][i] = True
        
        for i in range(L - 1):
            if s[i] == s[i + 1]:
                # a string of length two being a palindrom
                dp[i][i + 1] = True

        # now dp[m][n] = dp[m+1][n-1] if s[m] == s[n] 
        # the idea is if I know the solution to a substring(m+1, n-1) then I know if substring(m,n)
        # dp[m][n] means subtring s[m:n+1] is a palindrome or not
        # now to fill the dp we go from string of length 1 all the way to n 
        # that way we will be able to build larger string from smaller strings

        for l in range(3, L + 1):
            for m in range(L - l + 1):
                n = m + l - 1
                dp[m][n] = dp[m + 1][n - 1] and (s[m] == s[n])
        # now check for which m, n we can get the longest substring
        max_length = 0
        max_length_palindrome = ''
        for m in range(L):
            for n in range(m, L):
                if dp[m][n]:
                    if n - m + 1 > max_length:
                        max_length_palindrome = s[m:n + 1]
                        max_length = n - m + 1
        return max_length_palindrome