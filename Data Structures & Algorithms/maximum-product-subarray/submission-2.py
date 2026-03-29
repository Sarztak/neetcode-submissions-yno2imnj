class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = currMin = maxProd = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:
                currMax, currMin = currMin, currMax # because negative number changes sign
            currMax = max(num, currMax * num) # we start new array when single number exceeds the previous prod
            currMin = min(num, currMin * num)
            maxProd = max(maxProd, currMax)
        return maxProd