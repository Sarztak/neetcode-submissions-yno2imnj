class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        currMax = currMin = maxProd = nums[0]

        for i in range(1, n):
            if nums[i] < 0:
                currMax, currMin = currMin, currMax
            
            currMax = max(currMax*nums[i], nums[i])
            currMin = min(currMin*nums[i], nums[i])
            maxProd = max(maxProd, currMax)
        return maxProd