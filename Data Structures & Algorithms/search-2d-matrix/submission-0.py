class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ncol = len(matrix[0])
        nrow = len(matrix)
        def search(row, low, high):
            mid = (low + high) // 2
            if row >= nrow or low > high:
                return False
            if mid >= ncol:
                return search(row + 1, 0, ncol)
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                return search(row, mid + 1, high)
            elif matrix[row][mid] > target:
                return search(row, low, mid - 1)
            else:
                return search(row + 1, 0, ncol)
        
        return search(0, 0, ncol)

        