from collections import deque, Counter
from heapq import heapify, heappop, heappush
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cpu_cycle = 0
        freq_char = Counter(tasks)
        heap = [(-f, c) for c, f in freq_char.items()]
        heapify(heap)
        queue = deque()

        while heap or queue:
            if queue and queue[0][2] == cpu_cycle:
                f, task, cc = queue.popleft()
                heappush(heap, (f, task))
            if heap:
                f, task = heappop(heap)
                if f + 1 < 0:
                    queue.append([f + 1, task, cpu_cycle + n + 1])
            cpu_cycle += 1
        
        return cpu_cycle

        