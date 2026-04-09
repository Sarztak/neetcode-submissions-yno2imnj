class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = j = 0
        n = len(nums)
        freq = {}

        # the idea is that I count the frequency of numbers in a window of length k
        # so I expand the window till it reaches the length k and then once it become longer
        # I move i and also del that element from the frequency counter because it is out of date now
        # on a general note if I needed to count not just two but m occurances of the same number in 
        # the window then I would reduce the frequence rather than completely deleting the window

        # another important lesson here is that repeat the code and use the constrains verbatim
        # I got in trouble because I inverted the contrains and the tried to be clever by trying to write
        # less lines of code which just makes debugging harder, wastes time. 
        # just repeat the code as many times as logic gets repeated in different branches or else just make some function
        # but be intentional about the steps and put them in steps
        while j < n:
            if abs(i - j) <= k:
                if nums[j] in freq:
                    freq[nums[j]] += 1
                    if freq[nums[j]] == 2:
                        return True 
                else:
                    freq[nums[j]] = 1 
            else:
                if nums[i] in freq:
                    del freq[nums[i]]
                    i += 1
                if nums[j] in freq:
                    freq[nums[j]] += 1
                    if freq[nums[j]] == 2:
                        return True 
                else:
                    freq[nums[j]] = 1 
            j += 1
        return False