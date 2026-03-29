class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = []
        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                _, prev_day = stack.pop()
                result[prev_day] = i - prev_day
            stack.append((t, i))
        return result
        