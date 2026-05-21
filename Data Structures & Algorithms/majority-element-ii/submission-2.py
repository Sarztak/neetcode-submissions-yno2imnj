import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        The is again a problem that need special handling and has a weird 
        way of finding out who are likely elements, and then count the actual
        frequency of these elements. 

        The premise is this: if you have three elements that are all different, none of them can be the majority element appearing more than n/3 times. So you can throw all three away and the answer doesn't change — the majority element in the remaining array is still the majority element in the original array.
        That's the invariant. Every cancellation throws away one of each of three distinct elements, which cannot include a "real" majority element being thrown away more than a "fake" one.
        So after all cancellations, what's left must contain the real majority elements if they exist — because they couldn't have been cancelled more than the others.
        """

        n = len(nums)
        c1, c2 = None, None 
        count1, count2 = 0, 0

        for i in range(n):
            # be careful about the order 
            # cannot check count2 == 0 after checking count1 = 0 because
            # that will assign c1 and c2 to the same elements as in the case of
            # nums = [1 1 1 3 3 2 2 2]
            if count1 == 0:
                c1 = nums[i]
                count1 += 1
            elif c1 == nums[i]:
                count1 += 1
            elif count2 == 0:
                c2 = nums[i]
                count2 += 1
            elif c2 == nums[i]:
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        count1, count2 = 0, 0 
        for i in range(n):
            if nums[i] == c1:
                count1 += 1
            elif nums[i] == c2:
                count2 += 1

        ans = []    

        # do not use if c1 and... 
        # it will fail if c1 is zero, be intentional about None 
        if c1 is not None and count1 > math.floor(n / 3):
            ans.append(c1)
          
        if c2 is not None and count2 > math.floor(n / 3):
            ans.append(c2)
        
        return ans

        