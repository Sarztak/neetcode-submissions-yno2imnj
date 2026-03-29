from collections import deque, defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        adj = defaultdict(list)
        n = len(edges)
        in_degree = [0]*(n + 1)        
        
        for p, q in edges:
            adj[p].append(q)
            adj[q].append(p)
            in_degree[p] += 1
            in_degree[q] += 1

        que = deque(p for p in range(1, n + 1) if in_degree[p] == 1)

        while que:
            p = que.popleft()
            in_degree[p] -= 1  # this will make it zero if it was one

            for q in adj[p]:
                in_degree[q] -= 1
                if in_degree[q] == 1:
                    que.append(q)
        

        for p, q in reversed(edges): # because I want to find the last redundant edge
            if in_degree[p] == 2 and in_degree[q]:
                return [p, q]
