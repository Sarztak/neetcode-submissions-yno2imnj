class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        
        for i, [p, q] in enumerate(edges):
            adj[p].append((q, i))
            adj[q].append((p, -2))

        maxIndex = [-float('inf')]
        edges_to_remove = set()
        def dfs(child, parent):
            visited[child] = True

            for c, i in adj[child]:
                if c == parent:
                    continue
                if visited[c]:
                    if (child, c) not in edges_to_remove and i != -2:
                        edges_to_remove.add((child, c))
                        maxIndex[0] = max(i, maxIndex[0])
                    return
                dfs(c, child)
        
        for i in range(1, len(edges) + 1):
            visited = [False]*(len(edges) + 1)
            dfs(i, -1)
        
        return edges[maxIndex[0]]
        