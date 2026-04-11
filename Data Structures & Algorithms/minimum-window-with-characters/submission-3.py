import string
from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)

        freq = {c: 0 for c in string.ascii_letters}
        freq_q = Counter(t)

        i = j = 0
        min_len = n + 1 # length of string can never be more than itself
        min_len_str = ""
        while j < n:
            freq[s[j]] = freq[s[j]] + 1
            condition_met = True

            for k, v in freq_q.items():
                if freq[k] < v:
                    condition_met = False
                    break
            
            # now I need to jump till the position where condition fails
            while i <= j and (s[i] not in freq_q or (s[i] in freq_q and freq[s[i]] > freq_q[s[i]])):
                freq[s[i]] = max(0, freq[s[i]] - 1)
                i += 1

            # after the update of i the length needs to be calcuated again
            if condition_met and j - i + 1 < min_len:
                min_len = (j - i + 1)
                min_len_str = s[i: j + 1]
            j += 1

        return min_len_str

