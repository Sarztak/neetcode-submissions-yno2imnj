from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        As the AI overload (mythos) has confirmed using the heavenly power of 
        over 5 trillion parameters that this problem cannot be solved using
        sliding window and that there is another method called prefix sum with 
        hashing. the prefix sum is defined as prefix[j] is sum of elements from
        0 to j - 1; so prefix[1] = nums[0] prefix[2] = nums[0] + nums[1] and so on. 
        Now prefix[0] = 0 is an important case because it represents the sum of an empty
        subarray and it is important for when I count the number of prefix sums that have 
        certain sum. For this problem a dictionary stores the count of prefix sums that 
        have a certain value. 
        Now the sum of subarray from index i to j i
        """

        n = len(nums)
        count = 0
        s = 0
        d = defaultdict(int) 
        d[0] = 1 # the prefix sum of 0 has been seen once because I know an empty subarray exists
        for i in range(n):
            s += nums[i]
            count += d[s - k] # it is import to first check and then add to the dictionary because if k = 0 then
            d[s] += 1 # d[s] will be added first and that will increment the count by 1 which is not valid

        return count
