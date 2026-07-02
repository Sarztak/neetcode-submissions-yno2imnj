/**
 * // Definition for a QuadTree node.
 * class Node {
 *     constructor(val,isLeaf,topLeft,topRight,bottomLeft,bottomRight) {
 *         this.val = val;
 *         this.isLeaf = isLeaf;
 *         this.topLeft = topLeft;
 *         this.topRight = topRight;
 *         this.bottomLeft = bottomLeft;
 *         this.bottomRight = bottomRight;
 *     }
 * }
 */

class Solution {
    /**
     * @param {number[][]} grid
     * @return {Node}
     */
    foo(r1, r2, c1, c2, grid) {
        console.log(r1, r2, c1, c2);
        const set = new Set();
        for (let i = r1; i < r2 + 1; i ++) {
            for (let j = c1; j < c2 + 1; j++) {
                set.add(grid[i][j]);
            };
        };

        const s = [...set];
        const node = new Node(0, false, null, null, null, null);

        if (s.length == 2) {
            // this is not leaf node and further division of 
            // the grid is needed
            // isLeaf is set to false already and value does not matter
            const r12 = Math.floor((r1 + r2) / 2);
            const c12 = Math.floor((c1 + c2) / 2);
            node.topLeft = this.foo(r1, r12, c1, c12, grid);
            node.topRight = this.foo(r1, r12, c12 + 1, c2, grid);
            node.bottomLeft = this.foo(r12 + 1, r2, c1, c12, grid);
            node.bottomRight = this.foo(r12 + 1, r2, c12 + 1, c2, grid);
        } else if (s.length == 1) {
            // this is a leaf node because the values in the grid are all the same
            node.val = s[0];
            node.isLeaf = true;
        };

        return node;

    }
    construct(grid) {
        const r = grid.length;
        const c = grid[0].length;
        return this.foo(0, r - 1, 0, c - 1, grid);
    }
}
