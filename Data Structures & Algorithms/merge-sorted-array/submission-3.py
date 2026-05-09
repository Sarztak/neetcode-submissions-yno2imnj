class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        Such problems make me seems that I should just stop doing more problems
        I tried several different things, none of which worked and the problem 
        depended on a simple observation that instead of starting from the front
        start filling in from the back. I am just not too fond of 
        starting from the back, it seems too eager and rather animal like I suppose
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        while k >= 0:
            if i >= 0 and j >= 0:
                if nums1[i] >= nums2[j]:
                    nums1[k] = nums1[i]
                    i -= 1
                else:
                    nums1[k] = nums2[j]
                    j -= 1
            elif j >= 0 and i < 0:
                nums1[k] = nums2[j]
                j -= 1
            elif i >= 0 and j < 0:
                nums1[k] = nums1[i] 
                i -= 1
            
            k -= 1
        

        

