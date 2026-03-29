class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        preMap = {i:[] for i in range(numCourses)}
        for pre, cor in prerequisites:
            preMap[pre].append(cor)
        
        def dfs(pre):
            if pre in visited:
                return False
            if not preMap[pre]:
                return True
            
            visited.add(pre)
            for cor in preMap[pre]:
                if not dfs(cor):
                    return False
            visited.remove(pre)
            preMap[pre] = []
            return True

        for pre in range(numCourses):
            if not dfs(pre):
                return False
        return True
        