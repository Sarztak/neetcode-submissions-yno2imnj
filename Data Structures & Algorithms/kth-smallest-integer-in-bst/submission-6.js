/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     constructor(val = 0, left = null, right = null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    /**
     * @param {TreeNode} root
     * @param {number} k
     * @return {number}
     */
    // a trivial solution is to just collect all the values in the
    // increasing order. the smallest value is always the left child then the center value and then right child
    // then recursively collect all the values. 
    foo(node, vals) {
        if (!node) return [];
        const leftChildren = this.foo(node.left, vals);
        vals.push(node.val);
        const rightChildren = this.foo(node.right, vals);
        return vals;
    };

    kthSmallest(root, k) {
        let node = root;
        const stack = [];
        let ans = -1;
        let count = 0
        while (node || stack.length > 0) {
            while (node) {
                stack.push(node);
                node = node.left;
            }; // this will stop only when node becomes null

            node = stack.pop(); // get the first non-null node which will be the left most

            ans = node.val; // this will be the lowest value
            count ++;
            if (count == k) {
                return ans
            };
            // move to the right node; does not matter if it is null, next non null node will be popped out
            node = node.right; 
        }
    }
}
