class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = triplets.copy()
        for i in range(3):
            res = [triplet for triplet in res if triplet[i] <= target[i]]
        
        ans = [-float('inf')]*3
        for a, b, c in res:
            ans[0] = max(ans[0], a)
            ans[1] = max(ans[1], b)
            ans[2] = max(ans[2], c)

        return ans == target

        