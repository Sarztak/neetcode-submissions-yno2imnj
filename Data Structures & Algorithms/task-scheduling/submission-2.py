from collections import deque
from collections import Counter
from heapq import heapify, heappop, heappush

class Solution:
    """
    This solution is not going to work because it always processes sequentially. But that is not
    the only problem. What needs to be picked to minimize the count it the task that has the 
    hightest remaining count. Basically the same concept as greedy problem solving. Which does not 
    get solved just because queue is replaced with the heap.
    """
    # def leastInterval(self, tasks: List[str], n: int) -> int:
    #     time_count = 0
    #     seen = {}
    #     queue = deque(tasks)
    #     while queue:
    #         time_count += 1
    #         prev_len = len(queue)
    #         L = 0
    #         while queue and queue[0] in seen and time_count - seen[queue[0]] < n + 1 and L < prev_len:
    #             curr_task = queue.popleft()
    #             queue.append(curr_task)
    #             L += 1
    #         if L == prev_len:
    #             print('idle', end='-')
    #             continue
    #         curr_task = queue.popleft()
    #         seen[curr_task] = time_count
    #         print(curr_task, end='-')

    #     return time_count

    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = [(-c, t) for t, c in Counter(tasks).items()]
        heapify(heap)
        queue = deque()
        time_count = 0
        while heap or queue:
            time_count += 1
            if queue and queue[0][1] <= time_count:
                c, f, t = queue.popleft()
                heappush(heap, (c, t))
            if heap:
                c, t = heappop(heap)
                c += 1
                if c < 0:
                    queue.append((c, time_count + n + 1, t))

        return time_count











