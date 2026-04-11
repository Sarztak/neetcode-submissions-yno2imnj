from heapq import heapify, heappop, heappush
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        k = min(k, n) # this is no needed though given the constraints of the problem

        window = [(-nums[i], i) for i in range(k)] # I need a max heap so elements are stored as negative of their original values, greater number at top that way

        heapify(window)
        ans = []
        i, j = 0, k - 1 # first I output the answer and after that I update the pointer

        while j < n:
            # now here I need to check if whatever element is at the top is in the window or not and if it is not then keep on removing those elements
            while window:
                x, p = window[0]
                if p >= i:
                    ans.append(-x)
                    break 
                else:
                    heappop(window)

            # update the pointers need to keep the window length fixed
            i += 1
            j += 1

            if j < n: # this is to handle the edge case when j == n - 1 so that I don't go out of index
                heappush(window, (-nums[j], j))

        return ans
        