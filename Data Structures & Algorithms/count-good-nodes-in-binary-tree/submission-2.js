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
     * @return {number}
     */
    foo(node, max_val) {
        const c3 = node.val >= max_val ? 1: 0;

        max_val = Math.max(max_val, node.val);
        
        const c1 = node.left ? this.foo(node.left, max_val) : 0;
        const c2 = node.right ? this.foo(node.right, max_val): 0;

        return c1 + c2 + c3;
    }

    goodNodes(root) {
        // root cannot be null as given that there is at least one node
        return this.foo(root, -Infinity);
    }
}
