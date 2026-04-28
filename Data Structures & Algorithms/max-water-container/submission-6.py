class Solution:
    def maxArea(self, heights: List[int]) -> int:
        """
        There is no perfect explanation for this, or at least the one that satisfied me. 
        But I guess that is what you get for being dumb. 
        The logic as is expoused is this: given that for any pair i, j the smaller height limits
        the areas no matter what j might be, we can discard the smaller height index and move to the next index
        if the smaller height it i then we do i + 1 and if the smaller height is j then we do j - 1
        To break the cases where heights are equal I choose to move i forward. 
        It is difficult to understand how does this cover all the cases.
        """
        maxArea = 0
        i, j = 0, len(heights) - 1
        while i < j:
            maxArea = max(maxArea, (j - i) * min(heights[i], heights[j]))
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        
        return maxArea

