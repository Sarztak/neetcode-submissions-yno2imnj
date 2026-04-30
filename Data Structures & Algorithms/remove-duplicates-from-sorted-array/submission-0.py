class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        unique_nums = [nums[0]] # there is no empty input so this is okay to do

        i = 0
        j = 1

        while j < len(nums):
            if nums[i] != nums[j]:
                unique_nums.append(nums[j])
                i = j 
            j += 1
        
        nums[:len(unique_nums)] = unique_nums

        return len(unique_nums)
        