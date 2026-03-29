class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        nodes = [-c for c in Counter(tasks).values()]
        q = deque()
        heapq.heapify(nodes)
        time = 0
        while q or nodes:
            time += 1

            if not nodes:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(nodes)
                if cnt:
                    q.append([cnt, time + n])
            if q and time == q[0][1]:
                heapq.heappush(nodes, q.popleft()[0])
        return time

        