class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        L = len(nums)
        for i in range(L):
            for j in range(i + 1, L):
                for k in range(j + 1, L):
                    a, b, c = nums[i], nums[j], nums[k]
                    if a + b + c == 0:
                        new_triplet = sorted([a, b, c])
                        if new_triplet not in triplets:
                            triplets.append(new_triplet)
        return triplets
        

        