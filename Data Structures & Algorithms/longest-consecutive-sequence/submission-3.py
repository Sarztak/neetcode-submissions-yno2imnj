class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        """
        I was not able to uncover the solution myself and not that it has 
        been told to me it feel trivial. if n - 1 does not exists in the set 
        then n is the starting point and from that starting point we can 
        check the length of the longest sequence. If n - 1 exists then obviously
        n is not the starting point and that was the biggest problem in the case 
        finding the starting point which not that it has been told to me seems trivial 
        and now I can't unsee it
        """
        for n in s:
            if n - 1 not in s:
                curr_len = 1
                while n + 1 in s:
                    curr_len += 1
                    n += 1
                max_len = max(max_len, curr_len)
        
        return max_len
        