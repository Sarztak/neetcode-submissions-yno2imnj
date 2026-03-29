class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        q = deque()
        preCor = defaultdict(list)
        indegree = [0]*numCourses
        for c, p in prerequisites:
            preCor[p].append(c)
            indegree[c] += 1
        
        for c in range(numCourses):
            if not indegree[c]:
                q.append(c)
        
        while q:
            r = q.popleft()
            res.append(r)
            for c in preCor[r]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    q.append(c)
            
        return res if len(res) == numCourses else []
        