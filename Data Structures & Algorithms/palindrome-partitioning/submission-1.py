class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        def dfs(start, subset):
            if start == n:
                res.append(subset)

            for end in range(start + 1, n + 1):
                p = s[start:end]

                if p == p[::-1]:
                    dfs(end, subset + [p])
        dfs(0, [])
        return res
        