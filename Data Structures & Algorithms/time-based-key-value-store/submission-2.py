from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append([timestamp, value])

    def search(self, nums, target):
        # find the mid such that nums[mid] <= target < nums[mid + 1] for 0 <= mid <= n - 2
        n = len(nums)
        lo = 0
        hi = n - 1
        while lo <= hi:
            mid = (lo + hi) // 2 # initial guess
            if mid == n - 1 and nums[mid][0] <= target:
                return nums[mid][1]
            elif nums[mid][0] <= target < nums[mid + 1][0]:
                return nums[mid][1]
            elif target > nums[mid][0]:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def get(self, key: str, timestamp: int) -> str:
        if key in self.data:
            values = self.data[key]
            values = sorted(values, key=lambda x: x[0])
            searched_value = self.search(values, timestamp)
            if searched_value != -1: # timestamp is between 1 and 1000
                return searched_value
            else:
                return ""
        else:
            return ""
        
