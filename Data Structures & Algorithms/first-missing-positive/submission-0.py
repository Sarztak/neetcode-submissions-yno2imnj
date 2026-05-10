class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        aux = [0] * n

        """
        The plan is as follows the aux array is filled with zero, if any 
        positive number occurs I will place it in that aux if there is space
        so aux contain 1, 2, 3, ... at index 0, 1, 2... now if there is any 
        gap meaning the first index in the aux which is still zero will be
        the answer. In case aux is full then answer is n + 1. This is still
        constant space because the length of aux does not grow - it is fixed
        """

        for k in nums:
            if 1 <= k <= n:
                aux[k - 1] = k
        
        for i in range(n):
            if aux[i] == 0:
                return i + 1
        
        return n + 1
        



