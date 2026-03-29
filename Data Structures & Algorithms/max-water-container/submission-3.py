class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i, j = 0, len(heights) - 1

        while i < j:
            max_area = max(max_area, (j - i)*min(heights[j], heights[i]))
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area
        