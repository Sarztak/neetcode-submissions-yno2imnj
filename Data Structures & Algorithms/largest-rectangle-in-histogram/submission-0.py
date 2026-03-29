class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_area = 0
        for i in range(n):
            j = i
            while j < n and heights[j] >= heights[i]:
                j += 1
            
            wR = j - i - 1

            k = i
            while  k > -1 and heights[k] >= heights[i]:
                k -= 1
            
            wL = i - k - 1

            max_area = max(heights[i] * (wR + wL + 1), max_area)
        
        return max_area
