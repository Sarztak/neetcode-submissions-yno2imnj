class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
    
        self.matrix = matrix
        """
        This problem requires us to compute a 2D prefix sum before hand so that 
        when sumRegion is evoked the sum of the rectange can be found in the constant 
        time. So this does not really magically reduce the time complexity - it just pays
        the cost upfront so that there is no cost when sumRegion is evoked 
            
        The main problem is what is the definition of the prefix sum in this case
        prefix[i][j] is defined in the same sense as a 1D prefix sum so again in this 
        case i = 0 or j = 0 does means that no row or column has been selected so the
        prefix[0][j] or prefix[i][j] is zero. This is defined to be zero not computed to
        be zero. It cannot be derived. Then we first compute a 1D prefix sum for the first row 
        and the first column; then use that as base to obtain the prefix sum for the rest of
        the matrix as prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] + nums[i - 1][j - 1]
        however prefix[i - 1][j - 1] gets counted twice once while computing prefix[i][j - 1]
        and once while computing prefix[i - 1][j] so to prevent double counting we need to 
        minus prefix[i - 1][j - 1] 
        prefix[i][j] = prefix[i][j - 1] + prefix[i - 1][j] + nums[i - 1][j - 1] - prefix[i - 1][j - 1]
        now the prefix[i][j] is the sum of all the elements in the rectangle from (0, 0) to (i - 1, j - 1)
        eg prefix[2][1] means rectangle from (0, 0) to (1, 0) of the original matrix
        """

        m, n = len(self.matrix), len(self.matrix[0])
        self.prefixSumMatrix = [[0] * (n + 1) for _ in range(m + 1)] 
            
        # do for the first row and first column the 1D prefix sum
        for i in range(1, n + 1):
            self.prefixSumMatrix[1][i] = self.prefixSumMatrix[1][i - 1] + self.matrix[0][i - 1]
        
        for i in range(2, m + 1):
            self.prefixSumMatrix[i][1] = self.prefixSumMatrix[i - 1][1] + self.matrix[i - 1][0]
        
        for i in range(2, m + 1):
            for j in range(2, n + 1):
                self.prefixSumMatrix[i][j] = (
                    self.prefixSumMatrix[i][j - 1] + 
                    self.prefixSumMatrix[i - 1][j] - 
                    self.prefixSumMatrix[i - 1][j - 1] + 
                    self.matrix[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.prefixSumMatrix[row2 + 1][col2 + 1]
            + self.prefixSumMatrix[row1][col1]
            - self.prefixSumMatrix[row1][col2 + 1]
            - self.prefixSumMatrix[row2 + 1][col1]
        )



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)