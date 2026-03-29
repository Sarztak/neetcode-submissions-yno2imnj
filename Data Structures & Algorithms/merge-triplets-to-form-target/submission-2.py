class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x, y, z = target

        group = set()
        for t in triplets:
            if t[0] > x or t[1] > y or t[2] > z:
                continue
            
            for i, j in enumerate(t):
                if j == target[i]:
                    group.add(i)
        return len(group) == 3
        