class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        end = defaultdict(int)
        for i, c in enumerate(s):
            end[c] = i
        start = 0
        ans = []
        while start < len(s):
            e = end[s[start]]
            l = 0
            while True:
                unique = set(s[start:e + 1])
                unique.remove(s[start])
                if l == len(unique):
                    break
                else:
                    l = len(unique)
                for u in unique:
                    e = max(e, end[u])
            ans.append(e - start + 1)
            start = e + 1
        
        return ans
             

        