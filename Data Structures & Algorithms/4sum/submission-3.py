from typing import List, Tuple
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        def twoSum(i, j, nums, target):
            """
            I made a mistake initially: this method just check once if the target exists or not
            But there may be multiple combinations that make up to the same target and those need
            to be counted as well. Also I need to increase both m, and n when answer is found so
            that I don't get stuck in the loop
            """
            t = target - nums[i] - nums[j]
            m = j + 1
            n = len(nums) - 1
            ans = set()

            while m < n:
                if nums[m] + nums[n] == t:
                    ans.add((nums[i], nums[j], nums[m], nums[n]))
                    m += 1
                    n -= 1
                elif nums[m] + nums[n] < t:
                    m += 1
                else:
                    n -= 1
            return ans # now the set may be empty if nothing is found, and I need to unroll the set 
        
        nums = sorted(nums)

        """
        The AI overload has assured me that there is no better solution than O(n^3) that exists for this 
        problem, and I was trying to pluck my hairs in vain. The simpler solution is to fix two elements and then
        take a two sum approach to try and find the remaining elements that is all
        """
        answers = set()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans = twoSum(i, j, nums, target)
                if ans: # don't union with empty set
                    answers = answers.union(ans)
        return sorted([list(x) for x in answers])

