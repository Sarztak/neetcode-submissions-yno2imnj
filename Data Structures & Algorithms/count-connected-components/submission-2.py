class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == n - 1:
            return 1
        visited = set()
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        def dfs(i):
            
            visited.add(i)
            for j in graph[i]:
                if j in visited:
                    continue
                dfs(j)
        
        count = 0
        for i in range(n):
            if i not in visited:
                count += 1
                dfs(i)
        
        return count