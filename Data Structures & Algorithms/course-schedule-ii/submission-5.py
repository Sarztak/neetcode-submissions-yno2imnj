from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        in_degree = [0]*numCourses
        for course, pre in prerequisites:
            adj[pre].append(course)
            in_degree[course] += 1
        
        order = []
        que = deque(pre for pre in range(numCourses) if in_degree[pre] == 0)

        while que:
            pre = que.popleft()
            order.append(pre)
            numCourses -= 1
            for course in adj[pre]:
                in_degree[course] -= 1
                if in_degree[course] == 0:
                    que.append(course)

        return order if numCourses == 0 else []
            
        