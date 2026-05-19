class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixProdLeft = [1] * (n + 2)
        prefixProdRight = [1] * (n + 2)

        for i in range(1, n + 1):
            prefixProdLeft[i] = prefixProdLeft[i - 1] * nums[i - 1]
        
        for i in range(n, 0, -1):
            prefixProdRight[i] = prefixProdRight[i + 1] * nums[i - 1]
        
        output = [prefixProdLeft[i - 1] * prefixProdRight[i + 1] for i in range(1, n + 1)] 
        
        return output