from collections import defaultdict
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        cache = defaultdict(int)
        def get_key(l):
            return tuple(sorted(l))

        def dfs(set1, set2):
            k1 = get_key(set1)
            k2 = get_key(set2)
            if k1 not in cache:
                cache[k1] = sum(set1)
            if k2 not in cache:
                cache[k2] = sum(set2)

            if cache[k1] == cache[k2]:
                return True
            
            for i in range(len(set2)):
                s1 = set1 + [set2[i]]
                s2 = set2[:i] + set2[i + 1:]
                k1, k2 = get_key(s1), get_key(s2)
                
                if k1 in cache and k2 in cache:
                    if cache[k1] == cache[k2]:
                        return True
                    else:
                        continue
                else:
                    if dfs(s1, s2):
                        return True
                
            return False
        
        return dfs([], nums)
        