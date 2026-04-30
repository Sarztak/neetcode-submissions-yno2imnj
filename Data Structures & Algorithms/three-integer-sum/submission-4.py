class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Apparently, I solved 4sum before and the solution is similar but with just one less number
        """
        
        nums = sorted(nums)

        def twoSums(i, nums, target):
            m = i + 1
            n = len(nums) - 1
            ans = set()
            t = target - nums[i]
            while m < n:
                if nums[m] + nums[n] == t:
                    ans.add((nums[i], nums[m], nums[n]))
                    m += 1
                    n -= 1
                elif nums[m] + nums[n] < t:
                    m += 1
                else:
                    n -= 1
            
            return ans
        answers = set()
        target = 0 # there the target is just set to zero which is special case; target can be anything
        for i in range(len(nums)):
            ans = twoSums(i, nums, target)
            if ans:
                answers = answers.union(ans)
        
        return [list(x) for x in answers]

