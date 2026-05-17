from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        val_freq = [(k, v) for k, v in c.items()]
        val_freq = sorted(val_freq, key=lambda x: x[1], reverse=True) # sort by the frequency
        ans = [x[0] for x in val_freq[:k]]

        return ans
        