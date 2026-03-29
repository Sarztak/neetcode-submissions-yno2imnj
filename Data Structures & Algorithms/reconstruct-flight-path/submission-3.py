class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        for source, dest in tickets:
            graph[source].append(dest)
        
        for key in graph:
            graph[key].sort()
        
        itenary = []

        def dfs(airport):
            while graph[airport]:
                next_dest = graph[airport].pop(0)
                dfs(next_dest)
            itenary.append(airport)
        
        dfs("JFK")

        return itenary[::-1]