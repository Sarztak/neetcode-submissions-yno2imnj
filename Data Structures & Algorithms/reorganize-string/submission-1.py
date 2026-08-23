from collections import Counter, deque
from heapq import heapify, heappop, heappush
# the solution is exactly similar to task scheduling problem where one task should not appear unless time t has passed. Here in this case t = 2, and there is no idle cycle. If there is one, then we return empty string because it is not possible to process the string under the given constraints of the problem.

class Solution:
    def reorganizeString(self, s: str) -> str:
        timer = 0
        queue = deque()
        heap = [(-f, c) for c, f in Counter(s).items()]
        heapify(heap)
        ans = ""
        while queue or heap:
            timer += 1
            if queue and queue[0][2] <= timer:
                f, c, t = queue.popleft()
                heappush(heap, (f, c))
            if heap:
                f, c = heappop(heap)
                ans += c
                f += 1
                if f < 0:
                    queue.append((f, c, timer + 2))
            else:
                return ""
        return ans




        