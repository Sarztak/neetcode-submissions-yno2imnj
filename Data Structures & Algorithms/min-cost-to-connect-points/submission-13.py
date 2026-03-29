
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([dist, i, j])
    
        parent = list(range(n))
        rank = [0]*n

        def find(x):
            if parent[x] == x:
                return x
            parent[x] = find(parent[x])

            return parent[x]
        
        def union(x, y):
            rootx = find(x)
            rooty = find(y)

            if rootx < rooty:
                parent[rootx] = rooty
            elif rooty < rootx:
                parent[rooty] = rootx
            else:
                parent[rooty] = rootx
                rank[rootx] += 1
        
        def are_connected(x, y):
            return find(x) == find(y)

        
        edges.sort()

        MST = []
        minCost = 0

        for e, u, v in edges:
            if are_connected(u, v):
                continue
            
            union(u, v)
            minCost += e
            MST.append([u, v])
        
        return minCost




