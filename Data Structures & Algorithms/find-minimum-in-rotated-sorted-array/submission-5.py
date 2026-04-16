class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)

        lo = 0
        hi = n - 1

        """
        I can't believe I solved this problem in the first go, though I it took me about 1:45 hr to figure it out.
        The logic stems from an observation that solve any given binary search problem for some index situation flips
        In this case as we move from left to right the conditions with respect to index i and the end elements changes
        so for example for [3, 4, 5, 6, 1, 2] for each either element at the end are both less but at soon at you hit 
        the lowest element that situation changes. now to the left and to the right you have elements which are higher
        than you. But this does not actually help solve the problem. And I struggled to take this further. Another simple
        though was just locate the sorted part of the array and the answer is at the lower index. So to find which part
        to the left or to the right of the mid the array is sorted I easy to check which I implemented
        but then I realised that my condition have an implicit assumption that lo < mid < hi and if that is not the case
        then there is no answer. So I had to impose two extra conditions lo = hi which means there is just one element
        or hi = lo + 1 meaning there are just two element left in which case the answer is just the minimum of the two.
        The case lo = hi + 1 won't occur because the `while` loop will break otherwise. 
        I was not sure I had covered all the cases but this worked. I still don't digest this solution fully.
        The main lesson I learned was there are implicit assumptions that I make, which can be falsified so I need to test
        them and add conditions to take care of it.
        """
        while lo <= hi:
            mid = (lo + hi) // 2
            if lo == hi:
                return nums[lo]
            elif hi == lo + 1:
                return min(nums[lo], nums[hi])
            elif nums[lo] < nums[mid] < nums[hi]:
                return nums[lo]
            elif nums[lo] < nums[mid] and nums[mid] > nums[hi]:
                lo = mid
            elif nums[lo] > nums[mid] and nums[mid] < nums[hi]:
                hi = mid
        
        return -1 # solution failed, there is some condition that I didn't find