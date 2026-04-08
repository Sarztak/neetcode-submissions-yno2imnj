class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        subset = []
        a, b, c = target

        for x, y, z in triplets:
            if x > a or y > b or z > c:
                continue
            subset.append([x, y, z])

        if not subset:
            return False
        
        x = max(n[0] for n in subset)
        y = max(n[1] for n in subset)
        z = max(n[2] for n in subset)

        return True if x == a and y == b and z == c else False