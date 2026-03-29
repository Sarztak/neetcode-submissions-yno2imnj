class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prerec = {i : [] for i in range(numCourses)}
        for pre, cor, in prerequisites:
            prerec[pre].append(cor)
        
        visited = set()
        
        def dfs(pre):
            if pre in visited:
                return False
            if prerec[pre] == []:
                return True
            visited.add(pre)
            for p in prerec[pre]:
                if not dfs(p):
                    return False
            prerec[pre] = []
            visited.remove(pre)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        