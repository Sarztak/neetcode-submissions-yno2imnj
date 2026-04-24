class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxRight = [height[0]] * n # max while going to the right
        maxLeft = [height[-1]] * n # max while going to the left
        for i in range(1, n):
            maxRight[i] = max(maxRight[i - 1], height[i])
            maxLeft[-(i + 1)] = max(maxLeft[-(i + 1) + 1], height[-(i + 1)]) 

        water = 0
        for i in range(1, n - 1):
            if height[i] < maxRight[i] and height[i] < maxLeft[i]:
                water += min(maxRight[i], maxLeft[i]) - height[i]
        
        return water
