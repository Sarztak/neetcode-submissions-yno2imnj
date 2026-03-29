class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for n in range(len(nums)):
            nums[n] = nums[n]
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
        