class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr: List[int], target: int) -> bool:
            lo = 0
            hi = len(arr) - 1

            while lo <= hi:
                mid = (lo + hi) // 2
                
                if arr[mid] == target:
                    return True
                elif arr[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid - 1
            
            return False
        
        m = len(matrix)
        n = len(matrix[0])

        ri = 0
        rj = m - 1

        while ri <= rj:
            mid = (ri + rj) // 2

            if matrix[mid][0] == target:
                return True
            
            elif matrix[mid][0] < target:
                if matrix[mid][0] < target <= matrix[mid][n - 1]:
                    return binary_search(matrix[mid], target)
                ri = mid + 1
            else: # matrix[mid][0] > target:
                rj = mid - 1

        return False
        
"""
Again a good question to illustrate the principal of binary search
choose a guess and then reduce the search space. In this case the logic was 
to first use the column one to determine in which row the answer can be and the
use the regular 1d binary search to find the answer
"""









