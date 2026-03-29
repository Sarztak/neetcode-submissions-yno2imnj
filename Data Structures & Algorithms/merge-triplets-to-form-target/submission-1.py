class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        x, y, z = target

        for t in triplets:
            if t[0] > x or t[1] > y or t[2] > z:
                continue

            for i, e in enumerate(t):
                if e == target[i] :
                    good.add(i)
        return len(good) == 3