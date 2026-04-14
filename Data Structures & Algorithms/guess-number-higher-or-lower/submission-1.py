# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

# there are a couple of things to note about this question
# here the mid + 1 and mid - 1 are directly equal to the lo and hi
# and they are not been used as indexes to any array. 
# mid = (lo + hi) // 2 still works !!! though lo + hi can be an odd number
class Solution:
    def guessNumber(self, n: int) -> int:
        lo = 1
        hi = n 
        while lo <= hi:
            mid = (lo + hi) // 2

            if guess(mid) == 0:
                return mid
            elif guess(mid) == -1:
                hi = mid - 1
            else: 
                lo = mid + 1
    
        return (lo + hi) // 2
        