from collections import deque
from heapq import heapify, heappop, heappush
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        timer = 0
        queue = deque(sorted([(e, t, i) for i, (e, t) in enumerate(tasks)]))
        heap = []
        heapify(heap)
        ans = []

        while queue or heap:
            while queue and queue[0][0] <= timer:
                e, t, i = queue.popleft()
                # put in heap by time to complete, smallest, min heap, all those in heap are eligible to be completed
                heappush(heap, (t, i))
            if heap:
                t, i = heappop(heap)
                ans.append(i)
                timer += t
            else:
                # set the time to the next start rather than looping with timer ++ one step at a time, the effect is the same but several loops are saved.
                timer = queue[0][0] 
        return ans
