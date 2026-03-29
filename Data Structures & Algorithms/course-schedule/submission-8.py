from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # this is a brute force solution using dfs 
        # for each course which has prereq, I am trying to 
        # detect a cycle by storing the visited nodes
        # if I come across a node that I had already visited
        # then i have detected a cycle
        # I do this for every course, if there are not cycle
        # then I know I can take all the courses
        # the base case is those course which has no prereq.
        taken = [True]*numCourses
        coursePre = defaultdict(list)
        for course, pre in prerequisites:
            taken[course] = False # only those that have no prereq will be True hence taken
            coursePre[course].append(pre)
        

        def dfs(course, path):
            if taken[course]: 
                # this avoid key not exists in coursePre
                return True

            for pre in coursePre[course]:
                if pre in path or not dfs(pre, path + [pre]):
                    return False
            return True

        for course in coursePre:
            if dfs(course, [course]):
                taken[course] = True
            else:
                return False

        return True