class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m = len(s) # string
        n = len(p) # pattern

        # to note that we are considering dp to be the solution for the first i character
        # of s and first j characters of p so index for string at i will be i - 1 and so on
        dp = [[False]* (n + 1) for _ in range(m + 1)] # n + 1 col and m + 1 rows

        dp[0][0] = True # because we can match "" and ""

        # we can also match "" with a* 
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[0][j] = dp[0][j - 2] # j - 2 because we are matching "" with .* which can match empty string

        for i in range(1, m + 1): 
            for j in range(1, n + 1):
                if s[i - 1] == p[j - 1] or p[j - 1] == '.': 
                    # if there is exact match then we check for previous 
                    # characters matched or not 
                    dp[i][j] = dp[i-1][j-1]

                elif p[j - 1] == "*": 
                    # we can always match .* with "" so i - 1 matches with j - 3
                    dp[i][j] = dp[i][j - 2]

                    # given * which can match zero or more of what preceeds if
                    # there will be a match if p[j-2] == s[i - 1] or p[j-2] = '.' because
                    # then * will be equal to p[j - 2] so at position i - 1 and j - 1
                    # we will have a match
                    if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
        return dp[-1][-1]