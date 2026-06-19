class Solution {
    /**
     * @param {character[][]} board
     * @return {boolean}
     */
    isValidSudoku(board) {
        const m = board.length; // number of rows
        const n = board[0].length; // number of columns

        for (let i = 0; i < m; i ++) {
            const set = new Set();
            for (let j = 0; j < n; j ++) {
                if (board[i][j] == ".") continue 
                else if (set.has(board[i][j])) return false
                else set.add(board[i][j])
            }
        }

        for (let j = 0; j < n; j ++) {
            const set = new Set();
            for (let i = 0; i < m; i ++) {
                if (board[i][j] == ".") continue 
                else if (set.has(board[i][j])) return false
                else set.add(board[i][j])
            }
        }

        for (let i = 0; i < m; i = i + 3) {
            for (let j = 0; j < n; j = j + 3) {
                const set = new Set();
                for (let l = i; l < i + 3; l ++) {
                    for (let k = j; k < j + 3; k ++) {
                        if (board[l][k] == ".") continue 
                        else if (set.has(board[l][k])) return false
                        else set.add(board[l][k])
                    }
                }
            }
        }

        return true
    }
}
