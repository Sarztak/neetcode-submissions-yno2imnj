class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Build the graph and in-degree array
        graph = defaultdict(list)
        in_degree = [0] * numCourses
        
        for a, b in prerequisites:
            graph[b].append(a)  # b -> a
            in_degree[a] += 1   # a has one more prerequisite
        
        # Step 2: Initialize the queue with courses that have no prerequisites
        queue = deque()
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)
        
        # Step 3: Process the courses
        result = []
        while queue:
            course = queue.popleft()
            result.append(course)
            
            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)
        
        # Step 4: Check if we were able to take all courses
        if len(result) == numCourses:
            return result
        else:
            return []