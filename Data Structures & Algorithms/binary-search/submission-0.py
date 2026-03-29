class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(low, high):
            if low > high:
                return - 1
            mid = (high + low) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                return binary_search(mid + 1, high)
            else:
                return binary_search(low, mid - 1)
        
        return binary_search(0, len(nums) - 1)


        