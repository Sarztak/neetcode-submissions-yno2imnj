from heapq import heapify, heappop, heappush
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # one way to solve this problem is to just use heap over the distance and the elements themselves as a tuple
        # the array is already sorted and k <= len(arr)
        n = len(arr)

        distance = [(abs(x - a), a) for a in arr]

        # this should surface those elements that are at least distance from x and also if 
        # there are two or more elements with the same distance they the smallest one will be selected
        heapify(distance)

        # now simply remove the k element from the heap by popping themselves
        ans = []
        for _ in range(k):
            # since k <= n the heap won't get empty so I am not checking 
            ans.append(heappop(distance)[1])

        return sorted(ans) # sort the answer before returning