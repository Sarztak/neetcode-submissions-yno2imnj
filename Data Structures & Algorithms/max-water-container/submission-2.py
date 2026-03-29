class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        current_area = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            current_area = (j - i) * min(heights[i], heights[j])
            max_area = max(max_area, current_area)
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] <= heights[i]:
                j -= 1
        
        return max_area
        