class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        a, b, c = target
        max_a, max_b, max_c = [-float('inf')]*3
        for x, y, z in triplets:
            if x > a or y > b or z > c:
                continue
            max_a = max(max_a, x)
            max_b = max(max_b, y)
            max_c = max(max_c, z)

        return True if max_a == a and max_b == b and max_c == c else False