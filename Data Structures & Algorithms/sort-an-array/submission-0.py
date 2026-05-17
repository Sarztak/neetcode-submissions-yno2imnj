class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(arr1: List[int], arr2: List[int]) -> List[int]:
            l1, l2 = len(arr1), len(arr2)
            arr = [0] * (l1 + l2)
            i = j = k = 0

            while i < l1 and j < l2:
                if arr1[i] <= arr2[j]:
                    arr[k] = arr1[i]
                    i += 1
                else:
                    arr[k] = arr2[j]
                    j += 1
                k += 1
            
            if i == l1:
                arr[k:] = arr2[j:]
            elif j == l2:
                arr[k:] = arr1[i:]
            
            return arr

        # now repeatedly split and then merge the arrays 
        def sort(arr: List[int]) -> List[int]:
            if len(arr) == 1:
                return arr
            elif len(arr) == 2:
                return [min(arr[0], arr[1]), max(arr[0], arr[1])]
            mid = len(arr) // 2
            return merge(sort(arr[:mid]), sort(arr[mid:]))
        
        return sort(nums)