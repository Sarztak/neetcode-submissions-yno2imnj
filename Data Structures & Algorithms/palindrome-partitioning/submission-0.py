class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrom(t):
            return t == t[::-1]
        

        def dfs(start, subset):
            if start == len(s):
                res.append(subset.copy())
                return
            
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                if is_palindrom(substring):
                    subset.append(substring)
                    dfs(end, subset)
                    subset.pop()
        
        dfs(0, [])
        return res
        