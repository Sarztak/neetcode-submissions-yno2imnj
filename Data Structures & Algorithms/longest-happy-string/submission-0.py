from collections import deque
from heapq import heapify, heappop, heappush
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        timer = 0
        ans = ""
        queue = deque()
        chars = [(-a, "a"), (-b, "b"), (-c, "c")]
        heap = [(f, c) for f, c, in chars if f != 0]
        heapify(heap)
        while heap or queue:
            timer += 1
            if queue and queue[0][2] <= timer:
                f, c, t = queue.popleft()
                heappush(heap, (f, c))
            if heap:
                f, c = heappop(heap)
                if ans[-2:] != c * 2:
                    ans += c
                    f += 1
                    if f < 0:
                        heappush(heap, (f, c))
                else:
                    if f < 0:
                        queue.append((f, c, timer + 2))
            else:
                break 
        return ans

        