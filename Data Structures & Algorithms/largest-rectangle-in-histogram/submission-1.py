class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area_r = [0] * len(heights)
        area_l = [0] * len(heights)
        n = len(heights)
        for j, ch in enumerate(heights):
            while stack and stack[-1][1] > ch:
                i, h = stack.pop()
                a = (j - i) * h
                area_r[i] = a if a > 0 else 0
            stack.append((j, ch))

        for j, ch in stack:
            area_r[j] = (n - j) * ch 

        stack = []
        for j, ch in enumerate(heights[::-1]):
            while stack and stack[-1][1] > ch:
                i, h = stack.pop()
                a = (j - i) * h
                area_l[i] = a if a > 0 else 0
            stack.append((j, ch))

        for j, ch in stack:
            area_l[j] = (n - j) * ch 

        max_area = 0
        for i in range(n):
            total_area = area_r[i] + area_l[n - 1 - i] - heights[i]
            max_area = max(max_area, total_area)
        return max_area