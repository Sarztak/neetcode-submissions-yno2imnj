class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        speedDict = {}
        for i, p in enumerate(position):
            speedDict[p] = speed[i]

        position.sort()

        stack = []

        for curr in position:
            while stack:
                prev = stack[-1]
                ps = speedDict[prev]
                cs = speedDict[curr]
                if ps > cs:
                    t = (curr - prev) / (ps - cs)
                    if t <= (target - curr) / cs:
                        stack.pop()
                    else:
                        break
                else:
                    break
            stack.append(curr)

        return len(stack) 