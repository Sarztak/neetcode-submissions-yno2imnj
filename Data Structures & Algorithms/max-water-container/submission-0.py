class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = len(heights)
        max_area, current_area = 0, 0
        for i in range(L):
            for j in range(i + 1, L):
                current_area = (j - i) * min(heights[i], heights[j])
                max_area = max(max_area, current_area)
        return max_area
        