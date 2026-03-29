class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n - 1):
            return False

        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        visited = set()

        def dfs(neighbor, parent):
            if neighbor in visited:
                return False
            visited.add(neighbor)
            for n in graph[neighbor]:
                if n == parent:
                    continue
                if not dfs(n, neighbor):
                    return False
            return True
       
        return dfs(0, -1) and len(visited) == n 
        