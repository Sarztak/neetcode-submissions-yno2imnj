class NumMatrix {
    /**
     * @param {number[][]} matrix
     */
    constructor(matrix) {
        const m = matrix.length;
        const n = matrix[0].length;
        this.prefixSum2D = new Array(m).fill(null).map(() => new Array(n).fill(0));
        this.prefixSum2D[0][0] = matrix[0][0];
        for (let i = 1; i < n; i ++) {
            this.prefixSum2D[0][i] = this.prefixSum2D[0][i - 1] + matrix[0][i];
        }
        
        for (let i = 1; i < m; i ++) {
            this.prefixSum2D[i][0] = this.prefixSum2D[i - 1][0] + matrix[i][0];
        }

        for (let i = 1; i < m; i ++) {
            for (let j = 1; j < n; j ++) {
                this.prefixSum2D[i][j] = (
                    matrix[i][j] 
                    + this.prefixSum2D[i - 1][j] 
                    + this.prefixSum2D[i][j - 1] 
                    - this.prefixSum2D[i - 1][j - 1]
                );
            }
        }
    }

    /**
     * @param {number} row1
     * @param {number} col1
     * @param {number} row2
     * @param {number} col2
     * @return {number}
     */

    returnSum(row, col) {
        if (row < 0 || col < 0) return 0
        return this.prefixSum2D[row][col]
    }
    sumRegion(row1, col1, row2, col2) {
        return (
            this.returnSum(row2, col2) 
            - this.returnSum(row1 - 1, col2) 
            - this.returnSum(row2, col1 - 1) 
            + this.returnSum(row1 - 1, col1 - 1)
        );
    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * var obj = new NumMatrix(matrix)
 * var param_1 = obj.sumRegion(row1,col1,row2,col2)
 */
