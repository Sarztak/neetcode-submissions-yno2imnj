import string
class Solution:
    def numDecodings(self, s: str) -> int:
        alpha = string.ascii_uppercase
        letter_dict = {str(i + 1): c for i, c in enumerate(alpha)}
        def get_ways(s):
            n = len(s)
            if n == 1:
                if s[0] == '0':
                    return 0
                else:
                    if s in letter_dict:
                        return 1
            if n == 2:
                if s[1] == '0':
                    # since s = 'x0' and x can be 1..9
                    # it is better to use .get(s, 0)
                    # for example to handle s = '90'
                    if s in letter_dict:
                        return 1
                else:
                    count = 0
                    if s[0] in letter_dict and s[1] in letter_dict:
                        count += 1
                    if s in letter_dict:
                        count += 1
                    return count
            return 0 # this condition should not be reached
        n = len(s)
        if n < 3:
            return get_ways(s)

        dp = [0] * (n)
        dp[0] = get_ways(s[0])
        dp[1] = get_ways(s[:2])
        for i in range(2, n):
            dp[i] += dp[i - 2] if s[i - 1: i + 1] in letter_dict else 0
            print(dp)
            dp[i] += dp[i - 1] if s[i] in letter_dict else 0
        return dp[-1]
