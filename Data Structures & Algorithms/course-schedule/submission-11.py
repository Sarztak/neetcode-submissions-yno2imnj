from collections import deque, defaultdict
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        on_path = set()
        adjList = defaultdict(list)
        for course, pre in prerequisites:
            adjList[course].append(pre)
        

        def dfs(course):
            if course in visited:
                return True
            if course in on_path:
                return False

            on_path.add(course) # this is important, you are check from that node the path taken has cycles or not
            for pre in adjList[course]:
                if not dfs(pre):
                    return False
            on_path.remove(course)
            visited.add(course)
            return True
    
        for course in range(numCourses):
            if not dfs(course):
                return False # if cycle found
        
        return True # if no cycle found
