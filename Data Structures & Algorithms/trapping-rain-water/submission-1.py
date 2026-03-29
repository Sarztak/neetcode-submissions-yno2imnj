class Solution:
    def trap(self, height: List[int]) -> int:
        L = len(height)
        leftmax = [0]*L
        rightmax = [0]*L
        max_height = 0

        for i in range(L):
            max_height = max(max_height, height[i])
            leftmax[i] = max_height
        
        max_height = 0

        for i in range(1, L+1):
            max_height = max(max_height, height[-i])
            rightmax[-i] = max_height
        
        area = 0

        for i in range(L):
            area += (min(leftmax[i], rightmax[i]) - height[i])
        
        return area
            
        