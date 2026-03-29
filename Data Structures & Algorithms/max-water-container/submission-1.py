class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def area(i, j):
            return (j - i)*min(heights[i], heights[j])

        L = len(heights)
        max_area = 0
        i, j = 0, L - 1
        while i < j:
            max_area = max(max_area, area(i, j))
            if heights[i] < heights[j]:
                i += 1
            elif heights[j] <= heights[i]:
                j -= 1
        return max_area

            
        
        