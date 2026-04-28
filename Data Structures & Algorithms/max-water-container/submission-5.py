class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        i, j = 0, len(heights) - 1
        while i < j:
            maxArea = max(maxArea, (j - i) * min(heights[i], heights[j]))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxArea

