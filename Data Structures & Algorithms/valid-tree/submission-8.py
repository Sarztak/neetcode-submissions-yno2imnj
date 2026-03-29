from collections import deque, defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = defaultdict(list)
        
        for p, q in edges:
            adj[p].append(q)
            adj[q].append(p)
        
        visited = set()

        def dfs(child, parent):
            # how the algorithm is started is important here dfs(0, -1), so we need 
            # to visit first
            visited.add(child)

            for c in adj[child]:
                if c == parent:
                    continue
                if c in visited:
                    return False
                

                if not dfs(c, child):
                    return False

            return True         

        if not dfs(0, -1): # this means no cycle
            return False

        return len(visited) == n # this means all nodes are connected
        
        