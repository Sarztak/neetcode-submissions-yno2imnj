from collections import deque, defaultdict
from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        inDegree = [0]*numCourses
        adjList = defaultdict(list)

        for course, pre in prerequisites:
            inDegree[course] += 1
            adjList[pre].append(course)
        
        que = deque(pre for pre in range(numCourses) if inDegree[pre] == 0)

        while que:
            pre = que.popleft()
            numCourses -= 1

            for course in adjList[pre]:
                inDegree[course] -= 1

                if inDegree[course] == 0:
                    que.append(course)
        
        return numCourses == 0
         
    
        