from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for p, q in edges:
            adj[p].append(q)
            adj[q].append(p)
        
        visited = [False]*n

        def bfs(node):
            que = deque([node])
            while que:
                p = que.popleft()
                visited[p] = True
                for q in adj[p]:
                    if not visited[q]:
                        visited[q] = True
                        que.append(q)

        count = 0
        for i in range(n):
            if not visited[i]:
                bfs(i)
                count += 1
        
        return count

            
        