class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triplets = []
        nums.sort()

        for i, a in enumerate(nums):
            # since the array is sorted and we are considering all number after a
            # if a > 0 then it is not possible to get a zero sum since all the three
            # numbers will be positive
            if a > 0:
                break

            # to avoid duplicate triplets we need that at least one number in the triplet
            # is distinct, so we skip over the duplicate numbers in the beginning
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, h = i + 1, len(nums) - 1

            while l < h:
                b, c = nums[l], nums[h]

                if a + b + c > 0:
                    h -= 1
                elif a + b + c < 0:
                    l += 1
                else:
                    triplets.append([a, b, c])
                    l += 1
                    h -= 1
                    while l < h and nums[l] == nums[l - 1]:
                        l += 1
        
        return triplets

        