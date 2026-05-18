from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # another way to tackle this is what the AI overlord calls as bucket sort 
        # the idea is that bucket[i] will contains number with that frequency i
        # and then we scan from the back to get the top k elements
        # this solution is O(n) time complexity but only for finding elements
        # there is no way to remove the counting step and the space needed for it 
        c = Counter(nums)
        bucket = [[] for _ in range(n + 1)]

        for _k, v in c.items():
            bucket[v].append(_k)
        
        # count the elements until k becomes zero
        ans = []
        i = n
        while k != 0 and i > 0:
            if len(bucket[i]) != 0:
                # if the bucket is not empty then add its elements until k
                j = 0
                while k != 0 and j < len(bucket[i]):
                    ans.append(bucket[i][j])
                    j += 1
                    k -= 1
            i -= 1

        return ans

