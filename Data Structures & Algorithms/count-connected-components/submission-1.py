class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if len(edges) == n - 1:
            return 1
        
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        connected = 0
        visited = set()
        def dfs(neighbor):
            visited.add(neighbor)
            for nei in graph[neighbor]:
                if nei not in visited:
                    dfs(nei)
        for i in range(n):
            if i not in visited:
                dfs(i)
                connected += 1
        return connected