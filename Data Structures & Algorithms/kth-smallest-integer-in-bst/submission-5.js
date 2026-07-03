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
    foo(node, vals) {
        if (!node) return [];
        const leftChildren = this.foo(node.left, vals);
        vals.push(node.val);
        const rightChildren = this.foo(node.right, vals);
        return vals;
    };

    kthSmallest(root, k) {
        const sortedChildren = this.foo(root, []);
        if (sortedChildren.length < k) {
            return null; // this should not happen if algo is correct and k is less that total number of nodes
        };

        return sortedChildren[k - 1];
    }
}
