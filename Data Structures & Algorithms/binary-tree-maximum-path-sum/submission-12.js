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
    maxPathSum(root) {
        function foo(node) {
            if (!node) {
                return [-Infinity, 0];
            }

            const [leftMax, leftVal] = foo(node.left);
            const [rightMax, rightVal] = foo(node.right);

            const val = node.val + Math.max(leftVal, rightVal, 0);
            const max = Math.max(
                leftMax, 
                rightMax, 
                node.val + Math.max(leftVal, 0) + Math.max(rightVal, 0) 
            )

            return [max, val];
        };
        const [max] = foo(root);
        return max;
    }
}
