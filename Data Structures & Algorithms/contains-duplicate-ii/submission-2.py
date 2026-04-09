class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = j = 0
        n = len(nums)
        freq = {}
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