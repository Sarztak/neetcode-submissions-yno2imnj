class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
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
            for nei in graph[neighbor]:
                if nei == parent:
                    continue
                if not dfs(nei, neighbor):
                    return False
            return True
       
        return dfs(0, -1) and len(visited) == n 
        