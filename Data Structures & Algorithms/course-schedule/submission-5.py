from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        taken = [True]*numCourses
        coursePre = defaultdict(list)
        que = deque()
        visited = set()
        for course, pre in prerequisites:
            taken[course] = False # only those that have no prereq will be True hence taken
            coursePre[course].append(pre)
        

        def dfs(course, path):
            if taken[course]:
                return True

            
            for pre in coursePre[course]:
                if pre in path :
                    return False
                if not dfs(pre, path + [pre]):
                    return False
            return True

        for course in coursePre:
            if dfs(course, [course]):
                taken[course] = True
            else:
                return False

        return all(taken)