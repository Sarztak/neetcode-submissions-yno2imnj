class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        q = deque()
        indegree = [0]*(len(edges) + 1)
        graph = [[] for _ in range(len(edges) + 1)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            indegree[u] += 1
            indegree[v] += 1
        
        for i in range(1, len(edges) + 1):

            if indegree[i] == 1:
                q.append(i)
        
        while q:
            p = q.popleft()
            indegree[p] -= 1
            for n in graph[p]:
                indegree[n] -= 1
                if indegree[n] == 1:
                    q.append(n)
        
        for u, v in edges[::-1]:
            if indegree[u] == 2 and indegree[v]:
                return [u, v]
        return []
        

        