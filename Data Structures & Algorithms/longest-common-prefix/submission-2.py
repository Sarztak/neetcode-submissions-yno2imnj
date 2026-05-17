class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # python does not sort the strings by length by default
        # sort lexicographically and then by length 
        strs = sorted(strs, key=lambda s: (s, len(s)))

        # now just consider the first and last string
        i = 0
        n = min(len(strs[0]), len(strs[-1]))

        while i < n:
            if strs[0][i] != strs[-1][i]:
                break
            i += 1
        
        return strs[0][:i]
