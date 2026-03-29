from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        for p, q in edges:
            adj[p].append(q)
            adj[q].append(p)
        
        visited = [False]*n

        def dfs(child, parent):
            visited[child] = True
            for c in adj[child]:
                if c == parent or visited[c]: 
                    # if there is a cycle we don't want to loop again
                    continue    
                dfs(c, child)

        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i, -1)
                count += 1
        
        return count

            
        